import pandas as pd 
import random
from datetime import datetime, timedelta

suppliers = [
    "Tesla Parts Ltd",
    "Bosch Mobility",
    "Continental Supply",
    "Tata Components",
    "Mahindra Logistics"
]

products = [
    "EV Battery",
    "Brake System",
    "Tyre",
    "Motor Controller",
    "Sensor Module"
]

warehouses = [
    "New York",
    "Chicago",
    "Dallas",
    "California",
    "Toronto"
]

delivery_statuses = [
    "Delivered",
    "Delayed",
    "In Transit"
]

data = []

for i in range(1000):

    record = {
        "supplier_id": f"S{i+1}",
        "supplier_name": random.choice(suppliers),
        "product_type": random.choice(products),
        "inventory_count": random.randint(50, 500),
        "delivery_status": random.choice(delivery_statuses),
        "delivery_days": random.randint(1, 15),
        "warehouse_location": random.choice(warehouses),
        "shipment_cost": random.randint(1000, 10000),
        "order_quantity": random.randint(10, 100),
        "timestamp": datetime.now() - timedelta(days=random.randint(0, 30))
    }

    data.append(record)

df = pd.DataFrame(data)

df.to_csv("supply_chain_data.csv", index=False)

print("CSV file generated successfully!") 