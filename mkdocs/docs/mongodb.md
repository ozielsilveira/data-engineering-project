# MongoDB

## Descrição

O MongoDB é usado como a solução de banco de dados NoSQL para armazenar os dados brutos que são recebidos de várias fontes. Esta camada inicial é essencial para capturar os dados em seu formato original antes de qualquer processamento ou transformação.

## Objetivo

O objetivo do MongoDB no projeto é fornecer um armazenamento flexível e escalável para os dados brutos, facilitando a ingestão e a recuperação rápida desses dados para processamento subsequente.

## Estrutura de Dados

### Coleções

#### Criação das Coleções

```javascript
// Criar coleção de clientes
db.createCollection("Customer");

// Criar coleção de departamentos
db.createCollection("Department");

// Criar coleção de funcionários
db.createCollection("Employees");

// Criar coleção de pedidos
db.createCollection("Order");

// Criar coleção de produtos
db.createCollection("Product");

// Criar coleção de itens de pedidos
db.createCollection("OrderItem");

// Criar coleção de produtos de departamentos
db.createCollection("DepartmentProducts");
```

#### Inserção de Dados

```javascript
// Inserir documentos na coleção Customer
db.Customer.insertMany([
  {
    customerId: "75ecd863-79fb-4fb0-9327-9bbc2d9fb8ce",
    name: "Brenda Moore",
    address: "85358 Jacob Mall Suite 243\nWest Kevinview, NY 06029",
    email: "nataliegibson@example.net",
  },
]);

// Inserir documentos na coleção Department
db.Department.insertMany([
  {
    departmentId: "5dfef901-7fce-4adc-8b90-3d33d154e0ab",
    name: "Chen-Walker",
    location: "South Connor",
  },
]);

// Inserir documentos na coleção Employees
db.Employees.insertMany([
  {
    employeeId: "917c2c66-c252-4a46-9093-2703f452e708",
    name: "Elizabeth Thompson",
    position: "Oncologist",
    createdAt: "2024-03-10T15:40:23.367115",
    salary: 4232.44,
    departmentId: "4f87a6dd-ed90-45cb-9070-2015852dc0f9",
  },
]);

// Inserir documentos na coleção Order
db.Order.insertMany([
  {
    orderId: "a3b386cb-49fb-4b04-915c-ef6acda74b3d",
    customerId: "03537290-1f2f-4044-b4d0-8d8fc31c11e8",
    createdAt: "2022-06-23T16:40:50.876325",
    total: 0,
  },
]);

// Inserir documentos na coleção Product
db.Product.insertMany([
  {
    productId: "efedfafb-7c3c-40aa-8b3a-c15f752b60e3",
    name: "something",
    description:
      "Morning current why understand research plant place perhaps. Couple prove white.\nRepublican physical next cost.",
  },
]);

// Inserir documentos na coleção OrderItem
db.OrderItem.insertMany([
  {
    itemId: "496a7114-6e54-4c22-bf9d-5f1ee888b305",
    orderId: "bcd199af-37b2-498c-b5fb-2a7849b44d61",
    productId: "04d5f343-d5cc-494c-aa93-322bb8cf3e50",
    productName: "Product",
    quantity: 7,
    unitPrice: 331.83,
    totalPrice: 2322.81,
  },
]);

// Inserir documentos na coleção DepartmentProducts
db.DepartmentProducts.insertMany([
  {
    departmentProductId: "fccb2fd0-59f1-4575-98d4-f5a8bccfb68f",
    departmentId: "46b3838b-a0d1-423a-9ed8-03b23dfa340d",
    productId: "ead17aec-7dbc-4894-b548-19024513cdf2",
    costPrice: 44.56,
    sellingPrice: 587.39,
    stockQuantity: 39,
  },
]);
```

## Processos

### Ingestão de Dados

1. **Coleta de Dados**: Dados são coletados de várias fontes, como APIs, arquivos CSV, etc.
2. **Armazenamento no MongoDB**: Os dados são armazenados no MongoDB em coleções específicas para cada tipo de dado.

### Consultas de Exemplos

- **Consultas**:

  - Obter todos os clientes:

        ```javascript
        db.Customer.find({})
        ```

    - Obter todos os departamentos:

      ```javascript
      db.Department.find({});
      ```

    - Obter todos os funcionários:

      ```javascript
      db.Employees.find({});
      ```

    - Obter todas as ordens:

      ```javascript
      db.Order.find({});
      ```

    - Obter todos os produtos:

      ```javascript
      db.Product.find({});
      ```

    - Obter todos os itens de ordens:

      ```javascript
      db.OrderItem.find({});
      ```

    - Obter todos os produtos de departamentos:

      ```javascript
      db.DepartmentProducts.find({});
      ```

## Ferramentas Utilizadas

- **MongoDB Atlas**: Plataforma de banco de dados como serviço (DBaaS) para MongoDB.
- **MongoDB Compass**: Ferramenta GUI para visualizar e explorar dados no MongoDB.
- **Drivers MongoDB**: Usados para conectar e interagir com o MongoDB a partir de diferentes linguagens de programação.

[Voltar para a página inicial](index.md)

---

Se precisar de mais alguma coisa, estou à disposição!
