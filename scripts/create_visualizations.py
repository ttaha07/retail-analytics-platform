from collections import defaultdict
from datetime import datetime
from pathlib import Path
import csv

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


DATA_DIR = Path("data/sample")
OUTPUT_DIR = Path("visualizations")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ORDERS_FILE = DATA_DIR / "olist_orders_dataset.csv"
ORDER_ITEMS_FILE = DATA_DIR / "olist_order_items_dataset.csv"
OUTPUT_FILE = OUTPUT_DIR / "monthly_revenue.png"


def read_csv(file_path):
    if not file_path.exists():
        raise FileNotFoundError(
            f"Missing required file: {file_path}. "
            "Run scripts/generate_sample_data.py first."
        )

    with file_path.open("r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def currency_formatter(value, _):
    return f"${value:,.0f}"


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
        ).strftime("%b %Y")

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

    month_order = sorted(
        monthly_revenue.keys(),
        key=lambda month: datetime.strptime(month, "%b %Y"),
    )

    revenue = [monthly_revenue[month] for month in month_order]

    fig, ax = plt.subplots(figsize=(11, 6))

    ax.bar(month_order, revenue, alpha=0.75)
    ax.plot(month_order, revenue, marker="o", linewidth=2)

    for index, value in enumerate(revenue):
        ax.text(
            index,
            value,
            f"${value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.set_title("Monthly Revenue Trend", fontsize=16, fontweight="bold")
    ax.set_xlabel("Order Month")
    ax.set_ylabel("Revenue")
    ax.yaxis.set_major_formatter(FuncFormatter(currency_formatter))
    ax.grid(axis="y", alpha=0.3)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=160)
    plt.close()

    print(f"Created {OUTPUT_FILE}")


if __name__ == "__main__":
    create_monthly_revenue_chart()