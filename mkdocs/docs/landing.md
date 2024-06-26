# Camada Landing

## Descrição

A camada Landing é a primeira etapa do nosso pipeline de dados, onde os dados brutos são recebidos e armazenados. Nesta camada, os dados são coletados de várias fontes e mantidos em seu formato original, sem nenhuma transformação ou limpeza.

## Objetivo

O objetivo da camada Landing é garantir que todos os dados recebidos sejam armazenados de forma segura e íntegra para processamento posterior.

## Processos

1. **Ingestão de Dados**:
    - Coleta de dados de várias fontes (APIs, arquivos CSV, bancos de dados, etc.).
    - Armazenamento dos dados no MongoDB.

2. **Armazenamento**:
    - Os dados são armazenados no MongoDB em coleções específicas para cada fonte de dados.

## Estrutura de Dados
<!-- Incluir estrutura da camada Landing -->

## Ferramentas Utilizadas

- **MongoDB**: Para armazenamento dos dados brutos.
- **Scripts de Ingestão**: Scripts desenvolvidos em Python para coletar e armazenar os dados.

[Voltar para a página inicial](index.md)
