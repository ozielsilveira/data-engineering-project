# Camada Silver

## Descrição

A camada Silver é onde os dados são limpos e preparados para análises mais detalhadas. Nesta etapa, removemos duplicatas, corrigimos erros e preenchemos valores ausentes.

## Objetivo

O objetivo da camada Silver é garantir que os dados estejam limpos e prontos para análises avançadas.

## Processos

1. **Limpeza de Dados**:
    - Remoção de duplicatas.
    - Correção de valores inconsistentes.
    - Preenchimento de valores ausentes.

2. **Armazenamento**:
    - Os dados limpos são armazenados no Azure Synapse em tabelas otimizadas para análise.

## Documentação da Camada Silver

## Gerando Dataframes a partir do Delta Lake no Container Bronze do Azure Data Lake Storage

### Leitura dos Dados

```python
%%pyspark
df_products = spark.read.format("delta").load("abfss://bronze@datalakeengdados.dfs.core.windows.net/products")
df_customers = spark.read.format("delta").load("abfss://bronze@datalakeengdados.dfs.core.windows.net/customers")
df_departments = spark.read.format("delta").load("abfss://bronze@datalakeengdados.dfs.core.windows.net/departments")
df_orderItems = spark.read.format("delta").load("abfss://bronze@datalakeengdados.dfs.core.windows.net/orderItems")
df_orders = spark.read.format("delta").load("abfss://bronze@datalakeengdados.dfs.core.windows.net/orders")
df_employees = spark.read.format("delta").load("abfss://bronze@datalakeengdados.dfs.core.windows.net/employees")
df_departmentProducts = spark.read.format("delta").load("abfss://bronze@datalakeengdados.dfs.core.windows.net/departmentProducts")
```

### Adicionando Colunas de Metadata

```python
%%pyspark
from pyspark.sql.functions import current_timestamp, lit

df_products = df_products.withColumn("data_hora_silver", current_timestamp())
df_products = df_products.withColumn("nome_arquivo", lit("products"))

df_customers = df_customers.withColumn("data_hora_silver", current_timestamp())
df_customers = df_customers.withColumn("nome_arquivo", lit("customers"))

df_departments = df_departments.withColumn("data_hora_silver", current_timestamp())
df_departments = df_departments.withColumn("nome_arquivo", lit("departments"))

df_orderItems = df_orderItems.withColumn("data_hora_silver", current_timestamp())
df_orderItems = df_orderItems.withColumn("nome_arquivo", lit("orderItems"))

df_orders = df_orders.withColumn("data_hora_silver", current_timestamp())
df_orders = df_orders.withColumn("nome_arquivo", lit("orders"))

df_employees = df_employees.withColumn("data_hora_silver", current_timestamp())
df_employees = df_employees.withColumn("nome_arquivo", lit("employees"))
```

## Ajustando os Nomes das Colunas

### Products

```python
colunas_products = df_products.columns
print(colunas_products)

colunas_renomeadas_products = {
    '$oid': 'CODIGO',
    'productId': 'CODIGO_PRODUTO',
    'name': 'NOME',
    'description': 'DESCRICAO',
    'costPrice_$numberDouble': 'PRECO_CUSTO',
    'sellingPrice_$numberDouble': 'PRECO_VENDA',
    '$numberInt': 'QUANTIDADE',
    'data_hora_bronze': 'DATA_HORA_BRONZE',
    'data_hora_silver': 'DATA_HORA_SILVER',
    'nome_arquivo': 'NOME_ARQUIVO'
}

for old_name, new_name in colunas_renomeadas_products.items():
    df_products = df_products.withColumnRenamed(old_name, new_name)

display(df_products.limit(1))
```

### Salvando Dataframe Products na Camada Silver

```python
%%pyspark
silver_products = 'abfss://silver@datalakeengdados.dfs.core.windows.net/products'
df_products.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_products)
```

### Customers

```python
colunas_customers = df_customers.columns
print(colunas_customers)

colunas_renomeadas_customers = {
    '$oid': 'CODIGO',
    'customerId': 'CODIGO_CLIENTE',
    'name': 'NOME',
    'address': 'ENDERECO',
    'email': 'EMAIL',
    'data_hora_bronze': 'DATA_HORA_BRONZE',
    'data_hora_silver': 'DATA_HORA_SILVER',
    'nome_arquivo': 'NOME_ARQUIVO'
}

for old_name, new_name in colunas_renomeadas_customers.items():
    df_customers = df_customers.withColumnRenamed(old_name, new_name)

display(df_customers.limit(1))
```

### Salvando Dataframe Customers na Camada Silver

```python
%%pyspark
silver_customers = 'abfss://silver@datalakeengdados.dfs.core.windows.net/customers'
df_customers.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_customers)
```

### Employees

```python
colunas_employees = df_employees.columns
print(colunas_employees)

colunas_renomeadas_employees = {
    '$oid': 'CODIGO',
    'employeeId': 'CODIGO_FUNCIONARIO',
    'name': 'NOME',
    'position': 'CARGO',
    'createdAt': 'CADASTRADO',
    '$numberDouble': 'SALARIO',
    'departmentId': 'DEPARTAMENTO',
    'data_hora_bronze': 'DATA_HORA_BRONZE',
    'data_hora_silver': 'DATA_HORA_SILVER',
    'nome_arquivo': 'NOME_ARQUIVO'
}

for old_name, new_name in colunas_renomeadas_employees.items():
    df_employees = df_employees.withColumnRenamed(old_name, new_name)

display(df_employees.limit(1))
```

### Salvando Dataframe Employees na Camada Silver

```python
%%pyspark
silver_employees = 'abfss://silver@datalakeengdados.dfs.core.windows.net/employees'
df_employees.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_employees)
```

### Departments

```python
colunas_departments = df_departments.columns
print(colunas_departments)

colunas_renomeadas_departments = {
    '$oid': 'CODIGO',
    'departmentId': 'CODIGO_DEPARTAMENTO',
    'name': 'NOME',
    'location': 'LOCALIZACAO',
    'data_hora_bronze': 'DATA_HORA_BRONZE',
    'data_hora_silver': 'data_hora_silver',
    'nome_arquivo': 'NOME_ARQUIVO'
}

for old_name, new_name in colunas_renomeadas_departments.items():
    df_departments = df_departments.withColumnRenamed(old_name, new_name)

display(df_departments.limit(1))
```

### Salvando Dataframe Departments na Camada Silver

```python
%%pyspark
silver_departments = 'abfss://silver@datalakeengdados.dfs.core.windows.net/departments'
df_departments.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_departments)
```

### OrderItems

```python
colunas_orderItems = df_orderItems.columns
print(colunas_orderItems)

colunas_renomeadas_orderItems = {
    '$oid': 'CODIGO',
    'itemId': 'CODIGO_ITEM',
    'orderId': 'CODIGO_PEDIDO',
    'productId': 'CODIGO_PRODUTO',
    'productName': 'NOME_DO_PRODUTO',
    '$numberInt': 'QUANTIDADE',
    'unitPrice_$numberDouble': 'PRECO_UNITARIO',
    'totalPrice_$numberDouble': 'PRECO_TOTAL',
    'data_hora_bronze': 'DATA_HORA_BRONZE',
    'data_hora_silver': 'DATA_HORA_SILVER',
    'nome_arquivo': 'NOME_ARQUIVO'
}

for old_name, new_name in colunas_renomeadas_orderItems.items():
    df_orderItems = df_orderItems.withColumnRenamed(old_name, new_name)

display(df_orderItems.limit(1))
```

### Salvando Dataframe OrderItems na Camada Silver

```python
%%pyspark
silver_orderItems = 'abfss://silver@datalakeengdados.dfs.core.windows.net/orderItems'
df_orderItems.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_orderItems)
```

### Orders

```python
colunas_orders = df_orders.columns
print(colunas_orders)

colunas_renomeadas_orders = {
    '$oid': 'CODIGO',
    'orderId': 'CODIGO_PEDIDO',
    'customerId': 'CODIGO_CLIENTE',
    'orderDate': 'DATA_PEDIDO',
    'totalAmount_$numberDouble': 'VALOR_TOTAL',
    'data_hora_bronze': 'DATA_HORA_BRONZE',
    'data_hora_silver': 'DATA_HORA_SILVER',
    'nome_arquivo': 'NOME_ARQUIVO'
}

for old_name, new_name in colunas_renomeadas_orders.items():
    df_orders = df_orders.withColumnRenamed(old_name, new_name)

display(df_orders.limit(1))
```

### Salvando Dataframe Orders na Camada Silver

```python
%%pyspark
silver_orders = 'abfss://silver@datalakeengdados.dfs.core.windows.net/orders'
df_orders.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_orders)
```

[Voltar para a página inicial](index.md)
