from pathlib import Path
import csv
from datetime import datetime, timedelta


OUTPUT_DIR = Path("data/sample")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def write_csv(filename, fieldnames, rows):
    file_path = OUTPUT_DIR / filename

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created {file_path}")


customers = [
    {
        "customer_id": "C001",
        "customer_unique_id": "CU001",
        "customer_zip_code_prefix": "10001",
        "customer_city": "toronto",
        "customer_state": "ON",
    },
    {
        "customer_id": "C002",
        "customer_unique_id": "CU002",
        "customer_zip_code_prefix": "20002",
        "customer_city": "mississauga",
        "customer_state": "ON",
    },
    {
        "customer_id": "C003",
        "customer_unique_id": "CU003",
        "customer_zip_code_prefix": "30003",
        "customer_city": "hamilton",
        "customer_state": "ON",
    },
]

products = [
    {
        "product_id": "P001",
        "product_category_name": "electronics",
        "product_name_lenght": 12,
        "product_description_lenght": 80,
        "product_photos_qty": 2,
        "product_weight_g": 500,
        "product_length_cm": 20,
        "product_height_cm": 10,
        "product_width_cm": 15,
    },
    {
        "product_id": "P002",
        "product_category_name": "home_goods",
        "product_name_lenght": 14,
        "product_description_lenght": 95,
        "product_photos_qty": 3,
        "product_weight_g": 1200,
        "product_length_cm": 35,
        "product_height_cm": 20,
        "product_width_cm": 25,
    },
    {
        "product_id": "P003",
        "product_category_name": "fitness",
        "product_name_lenght": 10,
        "product_description_lenght": 70,
        "product_photos_qty": 1,
        "product_weight_g": 800,
        "product_length_cm": 30,
        "product_height_cm": 15,
        "product_width_cm": 20,
    },
]

base_date = datetime(2026, 1, 1, 10, 0, 0)

orders = [
    {
        "order_id": "O001",
        "customer_id": "C001",
        "order_status": "delivered",
        "order_purchase_timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
        "order_approved_at": (base_date + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_delivered_carrier_date": (base_date + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_delivered_customer_date": (base_date + timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_estimated_delivery_date": (base_date + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
        "order_id": "O002",
        "customer_id": "C002",
        "order_status": "delivered",
        "order_purchase_timestamp": (base_date + timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_approved_at": (base_date + timedelta(days=10, hours=1)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_delivered_carrier_date": (base_date + timedelta(days=11)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_delivered_customer_date": (base_date + timedelta(days=15)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_estimated_delivery_date": (base_date + timedelta(days=18)).strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
        "order_id": "O003",
        "customer_id": "C003",
        "order_status": "delivered",
        "order_purchase_timestamp": (base_date + timedelta(days=35)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_approved_at": (base_date + timedelta(days=35, hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_delivered_carrier_date": (base_date + timedelta(days=36)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_delivered_customer_date": (base_date + timedelta(days=40)).strftime("%Y-%m-%d %H:%M:%S"),
        "order_estimated_delivery_date": (base_date + timedelta(days=43)).strftime("%Y-%m-%d %H:%M:%S"),
    },
]

order_items = [
    {
        "order_id": "O001",
        "order_item_id": 1,
        "product_id": "P001",
        "seller_id": "S001",
        "shipping_limit_date": "2026-01-05 10:00:00",
        "price": 120.00,
        "freight_value": 12.50,
    },
    {
        "order_id": "O002",
        "order_item_id": 1,
        "product_id": "P002",
        "seller_id": "S002",
        "shipping_limit_date": "2026-01-15 10:00:00",
        "price": 250.00,
        "freight_value": 20.00,
    },
    {
        "order_id": "O003",
        "order_item_id": 1,
        "product_id": "P003",
        "seller_id": "S003",
        "shipping_limit_date": "2026-02-10 10:00:00",
        "price": 85.00,
        "freight_value": 9.99,
    },
]


write_csv(
    "olist_customers_dataset.csv",
    [
        "customer_id",
        "customer_unique_id",
        "customer_zip_code_prefix",
        "customer_city",
        "customer_state",
    ],
    customers,
)

write_csv(
    "olist_products_dataset.csv",
    [
        "product_id",
        "product_category_name",
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ],
    products,
)

write_csv(
    "olist_orders_dataset.csv",
    [
        "order_id",
        "customer_id",
        "order_status",
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ],
    orders,
)

write_csv(
    "olist_order_items_dataset.csv",
    [
        "order_id",
        "order_item_id",
        "product_id",
        "seller_id",
        "shipping_limit_date",
        "price",
        "freight_value",
    ],
    order_items,
)