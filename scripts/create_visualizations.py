from collections import defaultdict
from datetime import datetime
from pathlib import Path
import csv

import matplotlib.pyplot as plt


DATA_DIR = Path("data/sample")
OUTPUT_DIR = Path("visualizations")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


ORDERS_FILE = DATA_DIR / "olist_orders_dataset.csv"
ORDER_ITEMS_FILE = DATA_DIR / "olist_order_items_dataset.csv"
OUTPUT_FILE = OUTPUT_DIR / "monthly_revenue.png"


def read_csv(file_path):
    with file_path.open("r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def create_monthly_revenue_chart():
    orders = read_csv(ORDERS_FILE)
    order_items = read_csv(ORDER_ITEMS_FILE)

    order_month_lookup = {}

    for order in orders:
        order_id = order["order_id"]
        purchase_timestamp = order["order_purchase_timestamp"]
        order_month = datetime.strptime(
            purchase_timestamp,
            "%Y-%m-%d %H:%M:%S"
        ).strftime("%Y-%m")

        order_month_lookup[order_id] = order_month

    monthly_revenue = defaultdict(float)

    for item in order_items:
        order_id = item["order_id"]
        price = float(item["price"])
        freight_value = float(item["freight_value"])
        total_sale_amount = price + freight_value

        order_month = order_month_lookup.get(order_id)

        if order_month:
            monthly_revenue[order_month] += total_sale_amount

    months = sorted(monthly_revenue.keys())
    revenue = [monthly_revenue[month] for month in months]

    plt.figure(figsize=(10, 6))
    plt.plot(months, revenue, marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    plt.close()

    print(f"Created {OUTPUT_FILE}")


if __name__ == "__main__":
    create_monthly_revenue_chart()