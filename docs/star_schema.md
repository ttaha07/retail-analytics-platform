# Star Schema

The Gold layer centers on `FACT_SALES`, an order-item level fact table joined to customer, product, and date dimensions.

| Table | Grain | Key Columns |
|---|---|---|
| `FACT_SALES` | One row per order item | `SALES_SK`, `ORDER_ID`, `ORDER_ITEM_ID`, `CUSTOMER_UNIQUE_ID`, `PRODUCT_ID`, `TOTAL_SALE_AMOUNT` |
| `DIM_CUSTOMER` | One row per customer | `CUSTOMER_SK`, `CUSTOMER_ID`, `CUSTOMER_UNIQUE_ID`, `CUSTOMER_STATE` |
| `DIM_PRODUCT` | One row per product | `PRODUCT_SK`, `PRODUCT_ID`, `PRODUCT_CATEGORY_NAME` |
| `DIM_DATE` | One row per order date | `DATE_SK`, `ORDER_DATE`, `YEAR`, `MONTH` |

## Analytics Supported

| Query | Purpose |
|---|---|
| `monthly_revenue.sql` | Revenue trends over time. |
| `top_products.sql` | Product performance ranking. |
| `customer_retention.sql` | Cohort retention by first purchase month. |
| `regional_sales.sql` | Regional sales analysis. |