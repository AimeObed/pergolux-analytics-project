import random
import pandas as pd
from datetime import datetime, timedelta

random.seed(42)

products = [
    {"product_id": "P001", "product_name": "Pergola S", "category": "Pergola", "price": 1500},
    {"product_id": "P002", "product_name": "Pergola M", "category": "Pergola", "price": 1900},
    {"product_id": "P003", "product_name": "Pergola XL", "category": "Pergola", "price": 2300},
    {"product_id": "P010", "product_name": "LED Kit", "category": "Accessories", "price": 120},
    {"product_id": "P011", "product_name": "Side Wall", "category": "Accessories", "price": 250},
]
customers = []

countries = ["Germany", "France", "Netherlands", "Sweden", "Denmark"]

for i in range(1, 501):
    customer = {
        "customer_id": f"C{i:03d}",
        "country": random.choice(countries),
        "customer_type": random.choice(["Individual", "Business"])
    }
    customers.append(customer)
orders = []

start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 9, 30)

for i in range(1, 3001):
    random_days = random.randint(0, (end_date - start_date).days)
    order_date = start_date + timedelta(days=random_days)

    order = {
        "order_id": f"O{i:05d}",
        "customer_id": random.choice(customers)["customer_id"],
        "order_date": order_date.strftime("%Y-%m-%d")
    }

    orders.append(order)
order_items = []

for order in orders:
    number_of_items = random.randint(1, 3)
    selected_products = random.sample(products, number_of_items)

    for product in selected_products:
        order_item = {
            "order_id": order["order_id"],
            "product_id": product["product_id"],
            "quantity": random.randint(1, 3),
            "unit_price": product["price"]
        }

        order_items.append(order_item)
products_df = pd.DataFrame(products)
customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)
order_items_df = pd.DataFrame(order_items)

products_df.to_csv("data/products.csv", index=False)
customers_df.to_csv("data/customers.csv", index=False)
orders_df.to_csv("data/orders.csv", index=False)
order_items_df.to_csv("data/order_items.csv", index=False)