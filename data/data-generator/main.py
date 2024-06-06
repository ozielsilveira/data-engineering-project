import json
from faker import Faker
import random

fake = Faker()

def createCustomers(n):
    customers = []
    for _ in range(n):
        customer = {
            "customerId": str(fake.uuid4()),
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email()
        }
        customers.append(customer)
    with open('customers.json', 'w') as f:
        json.dump(customers, f, indent=4)

def createProducts(n):
    products = []
    for _ in range(n):
        cost_price = round(random.uniform(5, 500), 2)  # Preço de custo
        selling_price = round(cost_price * random.uniform(1.2, 2), 2)  # Preço de venda (20%-100% de margem de lucro)
        product = {
            "productId": str(fake.uuid4()),
            "name": fake.word(),
            "description": fake.text(),
            "costPrice": cost_price,
            "sellingPrice": selling_price,
            "stockQuantity": random.randint(0, 100)
        }
        products.append(product)
    with open('products.json', 'w') as f:
        json.dump(products, f, indent=4)

def createOrders(n, customer_ids):
    orders = []
    for _ in range(n):
        order = {
            "orderId": str(fake.uuid4()),
            "customerId": random.choice(customer_ids),
            "createdAt": fake.date_time_between(start_date="-3y", end_date="now").isoformat(),
            "total": 0  # O total será calculado posteriormente
        }
        orders.append(order)
    with open('orders.json', 'w') as f:
        json.dump(orders, f, indent=4)

def createOrderItems(n, order_ids, product_data):
    orderItems = []
    for _ in range(n):
        product = random.choice(product_data)
        item = {
            "itemId": str(fake.uuid4()),
            "orderId": random.choice(order_ids),
            "productId": product["productId"],
            "productName": product["name"],
            "quantity": random.randint(1, 10),
            "unitPrice": product["sellingPrice"],  # Usando o preço de venda
            "totalPrice": 0  # O total será calculado posteriormente
        }
        item["totalPrice"] = round(item["quantity"] * item["unitPrice"], 2)
        orderItems.append(item)
    with open('orderItems.json', 'w') as f:
        json.dump(orderItems, f, indent=4)

def createEmployees(n, department_ids):
    employees = []
    for _ in range(n):
        employee = {
            "employeeId": str(fake.uuid4()),
            "name": fake.name(),
            "position": fake.job(),
            "createdAt": fake.date_time_between(start_date="-3y", end_date="now").isoformat(),
            "salary": round(random.uniform(2000, 10000), 2),
            "departmentId": random.choice(department_ids)
        }
        employees.append(employee)
    with open('employees.json', 'w') as f:
        json.dump(employees, f, indent=4)

def createDepartments(n):
    departments = []
    for _ in range(n):
        department = {
            "departmentId": str(fake.uuid4()),
            "name": fake.company(),
            "location": fake.city()
        }
        departments.append(department)
    with open('departments.json', 'w') as f:
        json.dump(departments, f, indent=4)

def main():
    n = 10000
    
    createCustomers(n)
    
    with open('customers.json') as f:
        customers_data = json.load(f)
        customer_ids = [customer['customerId'] for customer in customers_data]
    
    createDepartments(n)
    
    with open('departments.json') as f:
        departments_data = json.load(f)
        department_ids = [department['departmentId'] for department in departments_data]
    
    createProducts(n)
    
    with open('products.json') as f:
        products_data = json.load(f)
    
    createOrders(n, customer_ids)
    
    with open('orders.json') as f:
        orders_data = json.load(f)
        order_ids = [order['orderId'] for order in orders_data]
    
    createEmployees(n, department_ids)
    
    with open('employees.json') as f:
        employees_data = json.load(f)
    
    createOrderItems(n, order_ids, products_data)

if __name__ == "__main__":
    main()
