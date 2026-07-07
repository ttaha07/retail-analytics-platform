# Star Schema

The Gold layer models retail data into a star schema centered on `FACT_SALES`. The fact table stores order-item level sales events and joins to customer, product, and date dimensions.

```mermaid
erDiagram
    FACT_SALES {
        number SALES_SK
        number CUSTOMER_SK
        number PRODUCT_SK
        number DATE_SK
        string ORDER_ID
        string ORDER_ITEM_ID
        string CUSTOMER_UNIQUE_ID
        number TOTAL_SALE_AMOUNT
    }

    DIM_CUSTOMER {
        number CUSTOMER_SK
        string CUSTOMER_ID
        string CUSTOMER_UNIQUE_ID
    }

    DIM_PRODUCT {
        number PRODUCT_SK
        string PRODUCT_ID
        string PRODUCT_CATEGORY_NAME
    }

    DIM_DATE {
        number DATE_SK
        date ORDER_DATE
        number YEAR
        number MONTH
    }

    DIM_CUSTOMER ||--o{ FACT_SALES : customer
    DIM_PRODUCT ||--o{ FACT_SALES : product
    DIM_DATE ||--o{ FACT_SALES : date