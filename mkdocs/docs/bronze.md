# Camada Bronze

## Descrição

Na camada Bronze, os dados brutos da camada Landing são transformados em um formato mais estruturado. Nesta etapa, os dados ainda podem conter duplicatas e erros, mas estão mais organizados.

## Objetivo

O objetivo da camada Bronze é realizar uma transformação inicial nos dados brutos para facilitar o processamento posterior.

## Código: utf-8

### Bronze

### **Listando todos os arquivos da camada Landing-Zone**

```python
landing_zone_path = "abfss://landing-zone@datalakeengdados.dfs.core.windows.net/"

df = spark.read.format("binaryFile").load(landing_zone_path)

file_paths = df.select("path").collect()
for file in file_paths:
    print(file["path"])
```

### **Products**

#### Gerando um dataframe (Products)

```python
df_products = spark.read.load('abfss://landing-zone@datalakeengdados.dfs.core.windows.net/products.parquet', format='parquet')
df_products.printSchema()
```

#### Adicionando metadados de data e hora de processamento e nome do arquivo de origem (Products)

```python
from pyspark.sql.functions import current_timestamp, lit

df_products = df_products.withColumn("data_hora_bronze", current_timestamp())
df_products = df_products.withColumn("nome_arquivo", lit("products.parquet"))
df_products.printSchema()
df_products.show(10)
```

#### Salvando na camada Bronze com o formato Delta

```python
bronze_products = 'abfss://bronze@datalakeengdados.dfs.core.windows.net/products'

df_products.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(bronze_products)
```

### **Customers**

#### Gerando um dataframe (Customers)

```python
df_customers = spark.read.load('abfss://landing-zone@datalakeengdados.dfs.core.windows.net/customers.parquet', format='parquet')
df_customers.printSchema()
```

#### Adicionando metadados de data e hora de processamento e nome do arquivo de origem (Customers)

```python
from pyspark.sql.functions import current_timestamp, lit

df_customers = df_customers.withColumn("data_hora_bronze", current_timestamp())
df_customers = df_customers.withColumn("nome_arquivo", lit("customers.parquet"))
df_customers.printSchema()
df_customers.show(10)
```

#### Salvando na camada Bronze com o formato Delta (Customers)

```python
bronze_customers = 'abfss://bronze@datalakeengdados.dfs.core.windows.net/customers'

df_customers.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(bronze_customers)
```

### **Departments**

#### Gerando um dataframe (Departments)

```python
df_departments = spark.read.load('abfss://landing-zone@datalakeengdados.dfs.core.windows.net/departments.parquet', format='parquet')
df_departments.printSchema()
```

#### Adicionando metadados de data e hora de processamento e nome do arquivo de origem (Departments)

```python
from pyspark.sql.functions import current_timestamp, lit

df_departments = df_departments.withColumn("data_hora_bronze", current_timestamp())
df_departments = df_departments.withColumn("nome_arquivo", lit("departments.parquet"))
df_departments.printSchema()
df_departments.show(10)
```

#### Salvando na camada Bronze com o formato Delta (Departments)

```python
bronze_departments = 'abfss://bronze@datalakeengdados.dfs.core.windows.net/departments'

df_departments.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(bronze_departments)
```

### **Employees**

#### Gerando um dataframe (Employees)

```python
df_employees = spark.read.load('abfss://landing-zone@datalakeengdados.dfs.core.windows.net/employees.parquet', format='parquet')
df_employees.printSchema()
```

#### Adicionando metadados de data e hora de processamento e nome do arquivo de origem (Employees)

```python
from pyspark.sql.functions import current_timestamp, lit

df_employees = df_employees.withColumn("data_hora_bronze", current_timestamp())
df_employees = df_employees.withColumn("nome_arquivo", lit("employees.parquet"))
df_employees.printSchema()
df_employees.show(10)
```

#### Salvando na camada Bronze com o formato Delta (Employees)

```python
bronze_employees = 'abfss://bronze@datalakeengdados.dfs.core.windows.net/employees'

df_employees.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(bronze_employees)
```

### **OrderItems**

#### Gerando um dataframe (OrderItems)

```python
df_orderItems = spark.read.load('abfss://landing-zone@datalakeengdados.dfs.core.windows.net/orderItems.parquet', format='parquet')
df_orderItems.printSchema()
```

#### Adicionando metadados de data e hora de processamento e nome do arquivo de origem (OrderItems)

```python
from pyspark.sql.functions import current_timestamp, lit

df_orderItems = df_orderItems.withColumn("data_hora_bronze", current_timestamp())
df_orderItems = df_orderItems.withColumn("nome_arquivo", lit("orderItems.parquet"))
df_orderItems.printSchema()
df_orderItems.show(10)
```

#### Salvando na camada Bronze com o formato Delta (OrderItems)

```python
bronze_orderItems = 'abfss://bronze@datalakeengdados.dfs.core.windows.net/orderItems'

df_orderItems.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(bronze_orderItems)
```

### **Orders**

#### Gerando um dataframe (Orders)

```python
df_orders = spark.read.load('abfss://landing-zone@datalakeengdados.dfs.core.windows.net/orders.parquet', format='parquet')
df_orders.printSchema()
```

#### Adicionando metadados de data e hora de processamento e nome do arquivo de origem (Orders)

```python
from pyspark.sql.functions import current_timestamp, lit

df_orders = df_orders.withColumn("data_hora_bronze", current_timestamp())
df_orders = df_orders.withColumn("nome_arquivo", lit("orders.parquet"))
df_orders.printSchema()
df_orders.show(10)
```

#### Salvando na camada Bronze com o formato Delta (Orders)

```python
bronze_orders = 'abfss://bronze@datalakeengdados.dfs.core.windows.net/orders'

df_orders.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(bronze_orders)
```

### **DepartmentProducts**

#### Gerando um dataframe (DepartmentProducts)

```python
df_departmentProducts = spark.read.load('abfss://landing-zone@datalakeengdados.dfs.core.windows.net/departmentProducts.parquet', format='parquet')
df_departmentProducts.printSchema()
```

#### Adicionando metadados de data e hora de processamento e nome do arquivo de origem (DepartmentProducts)

```python
from pyspark.sql.functions import current_timestamp, lit

df_departmentProducts = df_departmentProducts.withColumn("data_hora_bronze", current_timestamp())
df_departmentProducts = df_departmentProducts.withColumn("nome_arquivo", lit("departmentProducts.parquet"))
df_departmentProducts.printSchema()
df_departmentProducts.show(10)
```

#### Salvando na camada Bronze com o formato Delta (DepartmentProducts)

```python
bronze_departmentProducts = 'abfss://bronze@datalakeengdados.dfs.core.windows.net/departmentProducts'

df_departmentProducts.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(bronze_departmentProducts)
```

### **Validando a existência dos dados e das colunas dos metadados no Delta Lake**

```python
df_products = spark.read.load('abfss://bronze@datalakeengdados.dfs.core.windows.net/products', format='delta')
display(df_products.limit(2))
```

[Voltar para a página inicial](index.md)