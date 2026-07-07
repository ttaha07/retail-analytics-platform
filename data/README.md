# Data

This project uses the public Brazilian E-Commerce Olist dataset. The files in this folder are used for local development and Snowflake stage loading.

## Files

| File | Purpose |
|---|---|
| `olist_customers_dataset.csv` | Customer and location attributes. |
| `olist_orders_dataset.csv` | Order timestamps and status. |
| `olist_products_dataset.csv` | Product metadata. |
| `olist_order_items_dataset.csv` | Order-item level sales facts. |

The production pipeline loads these files into Snowflake Bronze tables, then transforms them into Silver and Gold models.