
# Camada Gold

## Descrição

A camada Gold é a etapa final do nosso pipeline de dados, onde os dados são refinados e otimizados para o consumo final por parte de sistemas de BI, como o Power BI.

## Objetivo

O objetivo da camada Gold é fornecer dados altamente estruturados e otimizados para análises detalhadas e criação de relatórios.

## Processos

1. **Refinamento de Dados**:
    - Agregação de dados.
    - Criação de métricas e indicadores chave.
    - Aplicação de transformações finais.

2. **Armazenamento**:
    - Os dados refinados são armazenados no Azure Synapse em tabelas otimizadas para consumo por ferramentas de BI.

## Estrutura de Dados

### Notebook 1: Gerando Dataframes

#### Gerando um dataframe dos delta lake no container silver do Azure Data Lake Storage.

```python
%%pyspark
df_products = spark.read.format("delta").load("abfss://silver@datalakeengdados.dfs.core.windows.net/products")
df_customers = spark.read.format("delta").load("abfss://silver@datalakeengdados.dfs.core.windows.net/customers")
df_departments = spark.read.format("delta").load("abfss://silver@datalakeengdados.dfs.core.windows.net/departments")
df_orderItems = spark.read.format("delta").load("abfss://silver@datalakeengdados.dfs.core.windows.net/orderItems")
df_orders = spark.read.format("delta").load("abfss://silver@datalakeengdados.dfs.core.windows.net/orders")
df_employees = spark.read.format("delta").load("abfss://silver@datalakeengdados.dfs.core.windows.net/employees")
df_departmentProducts = spark.read.format("delta").load("abfss://silver@datalakeengdados.dfs.core.windows.net/departmentProducts")
```

---

### Notebook 2: Criando a OBT

#### Criando uma OBT

```python
df_employees.createOrReplaceTempView("employees")
df_departments.createOrReplaceTempView("departments")
df_departmentProducts.createOrReplaceTempView("departmentProducts")
df_products.createOrReplaceTempView("products")
df_orderItems.createOrReplaceTempView("orderItems")
df_orders.createOrReplaceTempView("orders")
df_customers.createOrReplaceTempView("customers")

df_obt = spark.sql("""
SELECT p.CODIGO_PRODUTO, c.CODIGO_CLIENTE, d.CODIGO_DEPARTAMENTO, ot.CODIGO_PEDIDO, ot.QUANTIDADE,
e.CODIGO_FUNCIONARIO, e.SALARIO, dp.PRECO_CUSTO, dp.PRECO_VENDA
FROM employees AS e
INNER JOIN departments AS d ON e.DEPARTAMENTO = d.CODIGO_DEPARTAMENTO
INNER JOIN departmentProducts AS dp ON dp.CODIGO_DEPARTAMENTO = d.CODIGO_DEPARTAMENTO
INNER JOIN products AS p ON p.CODIGO_PRODUTO = dp.CODIGO_PRODUTO
INNER JOIN orderItems AS ot ON ot.CODIGO_PRODUTO = p.CODIGO_PRODUTO
INNER JOIN orders AS o ON o.CODIGO_PEDIDO = ot.CODIGO_PEDIDO
INNER JOIN customers AS c ON c.CODIGO_CLIENTE = o.CODIGO_CLIENTE
""")

display(df_obt.limit(1))
```

---

### Notebook 3: Salvando a OBT

#### Salvar a OBT em formato delta na camada gold.

```python
gold_obt = 'abfss://gold@datalakeengdados.dfs.core.windows.net/OBT'

df_obt.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(gold_obt)
```

---

### Notebook 4: Gerenciando Tabelas no Synapse

#### Remover tabela antiga, se existir

```sql
%%sql
DROP TABLE IF EXISTS tabela_obt_oficial;
```

#### Criar tabela nova

```sql
%%sql
CREATE TABLE IF NOT EXISTS tabela_obt_oficial
USING DELTA
LOCATION 'abfss://gold@datalakeengdados.dfs.core.windows.net/OBT'
```

## Visualização no Power BI

Os dados refinados na camada Gold são carregados no Power BI para criação de dashboards e relatórios interativos. Aqui estão alguns exemplos de visualizações:

[Voltar para a página inicial](index.md)