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
PRODUCTS_FILE = DATA_DIR / "olist_products_dataset.csv"
CUSTOMERS_FILE = DATA_DIR / "olist_customers_dataset.csv"

MONTHLY_REVENUE_OUTPUT = OUTPUT_DIR / "monthly_revenue.png"
CATEGORY_REVENUE_OUTPUT = OUTPUT_DIR / "revenue_by_category.png"
CITY_REVENUE_OUTPUT = OUTPUT_DIR / "revenue_by_city.png"


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


def load_sample_data():
    orders = read_csv(ORDERS_FILE)
    order_items = read_csv(ORDER_ITEMS_FILE)
    products = read_csv(PRODUCTS_FILE)
    customers = read_csv(CUSTOMERS_FILE)

    order_lookup = {order["order_id"]: order for order in orders}
    product_lookup = {product["product_id"]: product for product in products}
    customer_lookup = {customer["customer_id"]: customer for customer in customers}

    enriched_rows = []

    for item in order_items:
        order = order_lookup.get(item["order_id"])
        product = product_lookup.get(item["product_id"])

        if not order or not product:
            continue

        customer = customer_lookup.get(order["customer_id"])

        price = float(item["price"])
        freight_value = float(item["freight_value"])
        total_sale_amount = price + freight_value

        purchase_timestamp = datetime.strptime(
            order["order_purchase_timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        enriched_rows.append(
            {
                "order_id": item["order_id"],
                "order_month": purchase_timestamp.strftime("%b %Y"),
                "order_month_sort": purchase_timestamp,
                "product_category": product["product_category_name"],
                "customer_city": customer["customer_city"] if customer else "unknown",
                "total_sale_amount": total_sale_amount,
            }
        )

    return enriched_rows


def create_monthly_revenue_chart(rows):
    monthly_revenue = defaultdict(float)
    month_sort_lookup = {}

    for row in rows:
        monthly_revenue[row["order_month"]] += row["total_sale_amount"]
        month_sort_lookup[row["order_month"]] = row["order_month_sort"]

    months = sorted(monthly_revenue.keys(), key=lambda month: month_sort_lookup[month])
    revenue = [monthly_revenue[month] for month in months]

    fig, ax = plt.subplots(figsize=(11, 6))

    ax.bar(months, revenue, alpha=0.75)
    ax.plot(months, revenue, marker="o", linewidth=2)

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
    plt.savefig(MONTHLY_REVENUE_OUTPUT, dpi=160)
    plt.close()

    print(f"Created {MONTHLY_REVENUE_OUTPUT}")


def create_revenue_by_category_chart(rows):
    category_revenue = defaultdict(float)

    for row in rows:
        category_revenue[row["product_category"]] += row["total_sale_amount"]

    sorted_categories = sorted(
        category_revenue.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    categories = [item[0].replace("_", " ").title() for item in sorted_categories]
    revenue = [item[1] for item in sorted_categories]

    fig, ax = plt.subplots(figsize=(11, 6))

    ax.barh(categories, revenue, alpha=0.75)

    for index, value in enumerate(revenue):
        ax.text(
            value,
            index,
            f" ${value:,.0f}",
            va="center",
            fontsize=9,
        )

    ax.set_title("Revenue by Product Category", fontsize=16, fontweight="bold")
    ax.set_xlabel("Revenue")
    ax.set_ylabel("Product Category")
    ax.xaxis.set_major_formatter(FuncFormatter(currency_formatter))
    ax.grid(axis="x", alpha=0.3)

    ax.invert_yaxis()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(CATEGORY_REVENUE_OUTPUT, dpi=160)
    plt.close()

    print(f"Created {CATEGORY_REVENUE_OUTPUT}")


def create_revenue_by_city_chart(rows):
    city_revenue = defaultdict(float)

    for row in rows:
        city_revenue[row["customer_city"]] += row["total_sale_amount"]

    sorted_cities = sorted(
        city_revenue.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    cities = [item[0].title() for item in sorted_cities]
    revenue = [item[1] for item in sorted_cities]

    fig, ax = plt.subplots(figsize=(11, 6))

    ax.barh(cities, revenue, alpha=0.75)

    for index, value in enumerate(revenue):
        ax.text(
            value,
            index,
            f" ${value:,.0f}",
            va="center",
            fontsize=9,
        )

    ax.set_title("Revenue by Customer City", fontsize=16, fontweight="bold")
    ax.set_xlabel("Revenue")
    ax.set_ylabel("Customer City")
    ax.xaxis.set_major_formatter(FuncFormatter(currency_formatter))
    ax.grid(axis="x", alpha=0.3)

    ax.invert_yaxis()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(CITY_REVENUE_OUTPUT, dpi=160)
    plt.close()

    print(f"Created {CITY_REVENUE_OUTPUT}")


def main():
    rows = load_sample_data()

    create_monthly_revenue_chart(rows)
    create_revenue_by_category_chart(rows)
    create_revenue_by_city_chart(rows)


if __name__ == "__main__":
    main()