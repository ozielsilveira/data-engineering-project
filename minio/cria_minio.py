import os
import socket
from minio import Minio
from minio.versioningconfig import VersioningConfig
from dotenv import load_dotenv
from time import sleep as sp


################ Funções ################

# Instanciando o MinIO
def run_docker_compose():
    # Mudando para o diretório atual
    os.chdir(os.getcwd())

    buildCommand = f"docker-compose build"
    exec = os.system(buildCommand)

    if exec != 0:
        print(f"Ocorreu um erro o buildar o docker-compose: {exec}")
        exit()


    startCommand = "docker-compose -p data_lake up -d"
    exec = os.system(startCommand)

    if exec != 0:
        print(f"Ocorreu um erro ao rodar o container: {exec}")
        exit()

    return print("Docker rodando...")


# Valida portas em uso
def valida_porta(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

#########################################


# Executa o docker caso a porta 9000 (padrão MINIO) não estiver em uso
if (not valida_porta(9000)):
    run_docker_compose()
else:
    print("Já existe um serviço rodando na porta 9000")


# Tentando se conectar ao MinIO

try:
    load_dotenv()  # Pegando as variáveis de ambiente
    
    ACCESS_KEY =os.getenv("MINIO_ACCESS_KEY")
    SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
    HOST = os.getenv("MINIO_HOST")
    PORT = os.getenv("MINIO_PORT")

    minio_client = Minio(
        f"{HOST}:{PORT}",
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
        secure=False
    )

    bucket_names = ["landing", "bronze", "silver", "gold"]
    for i in bucket_names:
        if minio_client.bucket_exists(i):
            print(f"Bucket {i} já existe")
        else:
            minio_client.make_bucket(i)
            
            versioning_config = VersioningConfig("Enabled")  # Habilitando o versionamento do bucket
            minio_client.set_bucket_versioning(i, versioning_config)
            


    print("Conectou")

except:
    print("Houve um erro ao se conectar no MinIO")