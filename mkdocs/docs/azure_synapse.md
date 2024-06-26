# Azure Synapse

## Descrição

Azure Synapse é utilizado para processar e analisar grandes volumes de dados. Ele oferece um ambiente unificado para ingestão, preparação, gerenciamento e entrega de dados para BI e machine learning.

## Objetivo

O objetivo do Azure Synapse no projeto é fornecer uma plataforma robusta para processamento e transformação de dados, além de armazenar os dados processados em diferentes camadas (Bronze, Silver, Gold).

## Processos

### Pipeline de Dados

1. **Ingestão de Dados**: Dados brutos são exportados do MongoDB e ingeridos no Azure Synapse.
2. **Transformação Inicial (Bronze)**: Conversão de dados brutos em formatos estruturados.
3. **Limpeza de Dados (Silver)**: Remoção de duplicatas, correção de erros e preenchimento de valores ausentes.
4. **Refinamento de Dados (Gold)**: Criação de métricas e agregações para análise final.

## Ferramentas Utilizadas

- **Azure Synapse Studio**: Ambiente para desenvolvimento e gestão de pipelines de dados.
- **Apache Spark**: Para processamento de dados em grande escala.
- **SQL**: Para consultas e transformações de dados.

[Voltar para a página inicial](index.md)
