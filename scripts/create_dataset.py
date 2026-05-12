import pandas as pd
import random
from datetime import datetime, timedelta

products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"]
categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"]
regions = ["North", "South", "East", "West"]

data = []

start_date = datetime(2025, 1, 1)

for i in range(200):
    product_index = random.randint(0, 4)

    order_date = start_date + timedelta(days=random.randint(0, 365))

    quantity = random.randint(1, 5)

    sales = random.randint(500, 5000)

    profit = round(sales * random.uniform(0.1, 0.3), 2)

    data.append([
        order_date,
        products[product_index],
        categories[product_index],
        random.choice(regions),
        quantity,
        sales,
        profit
    ])

df = pd.DataFrame(data, columns=[
    "Order Date",
    "Product",
    "Category",
    "Region",
    "Quantity",
    "Sales",
    "Profit"
])

df.to_csv("../sales_data.csv", index=False)

print("Dataset created successfully!")