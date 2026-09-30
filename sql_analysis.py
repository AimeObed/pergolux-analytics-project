import sqlite3
import pandas as pd

connection = sqlite3.connect("pergolux.db")

products = pd.read_csv("data/products.csv")
customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")

products.to_sql("products", connection, if_exists="replace", index=False)
customers.to_sql("customers", connection, if_exists="replace", index=False)
orders.to_sql("orders", connection, if_exists="replace", index=False)
order_items.to_sql("order_items", connection, if_exists="replace", index=False)

query = """
SELECT
    p.product_name,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;
"""
result = pd.read_sql_query(query, connection)
print(result)

query = """
SELECT
    c.country,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY revenue DESC;
"""

result = pd.read_sql_query(query, connection)
print(result)

query = """
SELECT
    AVG(order_revenue) AS average_order_value
FROM (
    SELECT
        order_id,
        SUM(quantity * unit_price) AS order_revenue
    FROM order_items
    GROUP BY order_id
);
"""

result = pd.read_sql_query(query, connection)
print(result)

query = """
SELECT
    SUBSTR(o.order_date, 1, 7) AS month,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
GROUP BY month
ORDER BY month;
"""

result = pd.read_sql_query(query, connection)
print(result)