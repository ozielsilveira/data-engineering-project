# Desenvolvimento de uma Pipeline de Dados utilizando Azure Synapse

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Este projeto abrange todo o processo de construção de uma robusta pipeline de dados, desde a criação inicial do banco de dados MongoDB até a apresentação dos dados em Power BI. As principais etapas incluem:

- **Criação do Banco de Dados MongoDB**: Configuração e implementação de um banco de dados MongoDB, incluindo a elaboração de scripts para a população inicial dos dados.

- **Ingestão de Dados**: Importação dos dados brutos para o sistema, garantindo a integridade e a qualidade das informações desde a origem.

- **Data Lake**: Armazenamento dos dados em um Data Lake, utilizando as melhores práticas para organização e acessibilidade dos dados.

- **Transformações de Dados**: Aplicação de transformações nos dados através do Apache Spark, utilizando a arquitetura de medalhão para estruturar os dados em camadas (bronze, silver e gold).

- **Integração com Power BI**: Conexão e visualização dos dados transformados no Power BI, permitindo a criação de dashboards interativos e relatórios detalhados.

Este trabalho visa não apenas a construção de uma pipeline eficiente e escalável, mas também a garantia de que cada etapa do processo seja executada com precisão e alinhada às melhores práticas da engenharia de dados.

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

## Desenho de Arquitetura

Coloque uma imagem do seu projeto, como no exemplo abaixo:

![image](https://github.com/jlsilva01/projeto-ed-satc/assets/484662/541de6ab-03fa-49b3-a29f-dec8857360c1)

## Visão geral
- O ambiente relacional – origem – tem 7 tabelas, 10.000 linhas para cada tabela principal.
- Foi utilizado a biblioteca Faker do Python, para gerar as massas de dados e popular o ambiente relacional.
- A ingestão dos dados foi feita através do Azure Synapse Analytics
- O Data Lake foi criado em cima de um object storage (cloud) usando a arquitetura medalhão (Camadas Landing, Bronze, Silver e Gold).
- Os dados serão gravados no object storage no formato Delta Lake nas camadas Bronze, Silver e Gold.
  A transformação será feita através do Apache Spark (Python/pyspark).
- As funções de ingestão, transformação e movimentação dos dados entre as camadas são
  orquestradas e agendadas através da ferramenta Azure Synapse Analytics.
- Os dados serão disponibilizados na camada Gold no formato dimensional (OBT).
- Foram utilizadas 4 KPIs e 2 métricas para compor o dashboard no PowerBi.
- O dashboard consome os dados do modelo OBT, direto da camada gold.
- A documentação completa do trabalho está publicada no MkDocs.

## Implantação

## Terraform
Abra o CMD na pasta do projeto e execute os seguintes passos:

<br>Faça login na Azure usando o Azure CLI:
```bash
az login
```
Abrir o diretório onde está localizado o arquivo "main.tf"
```bash
terraform init
```
Crie um plano de execução para a infraestrutura:
```bash
terraform plan
```
Aplique o plano para criar os recursos na Azure
```bash
terraform apply
```

## Ferramentas utilizadas

- **[Azure](https://portal.azure.com/)** - é a plataforma de computação em nuvem da Microsoft que oferece uma ampla gama de serviços, incluindo computação, armazenamento, bancos de dados, redes e inteligência artificial, para desenvolver, gerenciar e hospedar aplicativos e serviços de maneira escalável e segura.
- **[Power BI](https://www.microsoft.com/pt-br/power-platform/products/power-bi)** - é uma ferramenta de business intelligence da Microsoft que permite a visualização interativa de dados e a criação de relatórios e dashboards dinâmicos, ajudando as empresas a transformar dados brutos em insights acionáveis de forma fácil e intuitiva.
- **[MongoDB](https://www.mongodb.com/)** - é um banco de dados NoSQL orientado a documentos que armazena dados em formato JSON-like, conhecido por sua flexibilidade, escalabilidade e facilidade de uso, sendo amplamente utilizado para aplicações modernas que exigem alta performance e gerenciamento eficiente de grandes volumes de dados não estruturados.

## Colaboração
Se desejar publicar suas modificações em um repositório remoto no GitHub, siga estes passos:

1. Crie um novo repositório vazio no GitHub.
2. No terminal, navegue até o diretório raiz do projeto.
3. Execute os seguintes comandos:

```bash
git remote set-url origin https://github.com/seu-usuario/nome-do-novo-repositorio.git
git add .
git commit -m "Adicionar minhas modificações"
git push -u origin master
```

Isso configurará o repositório remoto e enviará suas modificações para lá.

## Collaborators

- **Aluno 1** - _Criação do MongoDB e script de geração de dados_ - [Guilherme Santana](https://github.com/guirms)
- **Aluno 2** - _Ingestão de dados e Orquestração_ - [Jean Carlos Nesi](https://github.com/JeanNesi)
- **Aluno 3** - _Script Spark_ - [Bruna Savi](https://github.com/brsavii)
- **Aluno 4** - _Configurar ambiente Data Lake_ - [Luigi Milanez](https://github.com/luigimilanez)
- **Aluno 5** - _Métricas_ - [Lucas Borges Borba](https://github.com/lucasborba111)
- **Aluno 6** - _Power BI_ - [Kauã Librelato](https://github.com/KauaLibrelato)
- **Aluno 7** - _Documentação_ - [Oziel Silveira](https://github.com/ozielsilveira)

Você também pode ver a lista de todos os [colaboradores](https://github.com/ozielsilveira/data-engineering-project/colaboradores) que participaram deste projeto.

## Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE](https://github.com/jlsilva01/projeto-ed-satc/blob/main/LICENSE) para detalhes.

## Referências

[ChatGPT](https://chatgpt.com/)
[DatasideCommunity](https://www.youtube.com/@DatasideCommunity)
[Datasen](https://www.datensen.com/blog)

