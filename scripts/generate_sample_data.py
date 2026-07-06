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
        "customer_id": f"C{i:03}",
        "customer_unique_id": f"CU{i:03}",
        "customer_zip_code_prefix": f"{10000 + i}",
        "customer_city": city,
        "customer_state": "ON",
    }
    for i, city in enumerate(
        [
            "toronto",
            "mississauga",
            "hamilton",
            "brampton",
            "oakville",
            "burlington",
            "markham",
            "vaughan",
        ],
        start=1,
    )
]


# The original Olist dataset uses the misspelled column names
# product_name_lenght and product_description_lenght.
# These names are intentionally preserved so sample CSVs match the source schema.
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
    {
        "product_id": "P004",
        "product_category_name": "beauty",
        "product_name_lenght": 11,
        "product_description_lenght": 60,
        "product_photos_qty": 2,
        "product_weight_g": 300,
        "product_length_cm": 18,
        "product_height_cm": 8,
        "product_width_cm": 12,
    },
    {
        "product_id": "P005",
        "product_category_name": "office",
        "product_name_lenght": 9,
        "product_description_lenght": 75,
        "product_photos_qty": 2,
        "product_weight_g": 700,
        "product_length_cm": 25,
        "product_height_cm": 10,
        "product_width_cm": 18,
    },
]


base_date = datetime(2026, 1, 5, 10, 0, 0)

order_plan = [
    # month offset, customer_id, product_id, price, freight_value
    (0, "C001", "P001", 120.00, 12.50),
    (0, "C002", "P002", 250.00, 20.00),
    (0, "C003", "P003", 85.00, 9.99),
    (0, "C004", "P004", 65.00, 7.50),

    (1, "C005", "P001", 145.00, 13.00),
    (1, "C006", "P003", 95.00, 10.25),
    (1, "C007", "P005", 180.00, 14.00),
    (1, "C008", "P002", 275.00, 22.00),

    (2, "C001", "P004", 72.00, 8.00),
    (2, "C003", "P003", 115.00, 11.00),
    (2, "C005", "P001", 160.00, 15.00),
    (2, "C007", "P005", 210.00, 16.00),

    (3, "C002", "P002", 300.00, 24.00),
    (3, "C004", "P004", 88.00, 8.25),
    (3, "C006", "P003", 130.00, 12.00),
    (3, "C008", "P001", 175.00, 15.50),

    (4, "C001", "P005", 225.00, 18.00),
    (4, "C003", "P002", 320.00, 25.00),
    (4, "C005", "P003", 150.00, 13.50),
    (4, "C007", "P004", 95.00, 9.00),

    (5, "C002", "P001", 190.00, 16.00),
    (5, "C004", "P002", 340.00, 26.00),
    (5, "C006", "P003", 165.00, 14.00),
    (5, "C008", "P005", 260.00, 20.00),
]


orders = []
order_items = []

for index, (month_offset, customer_id, product_id, price, freight_value) in enumerate(
    order_plan,
    start=1,
):
    order_id = f"O{index:03}"
    purchase_timestamp = base_date + timedelta(days=month_offset * 30 + index)

    orders.append(
        {
            "order_id": order_id,
            "customer_id": customer_id,
            "order_status": "delivered",
            "order_purchase_timestamp": purchase_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "order_approved_at": (purchase_timestamp + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "order_delivered_carrier_date": (purchase_timestamp + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "order_delivered_customer_date": (purchase_timestamp + timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S"),
            "order_estimated_delivery_date": (purchase_timestamp + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

    order_items.append(
        {
            "order_id": order_id,
            "order_item_id": 1,
            "product_id": product_id,
            "seller_id": f"S{((index - 1) % 4) + 1:03}",
            "shipping_limit_date": (purchase_timestamp + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "price": price,
            "freight_value": freight_value,
        }
    )


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