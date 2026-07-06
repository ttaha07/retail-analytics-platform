# dbt Retail Analytics Layer

This folder contains an optional dbt implementation for the Retail Analytics Platform.

The dbt layer demonstrates analytics engineering concepts including:

- Source definitions
- Staging models
- Mart models
- Dimensional modeling
- Fact and dimension tables
- Schema tests
- Model documentation
- Monthly revenue analytics

The dbt layer is optional and does not replace the main Snowflake SQL pipeline.

## Model Flow

```text
SILVER source tables
    -> staging models
    -> marts models
    -> analytics models
```

## Models

```text
models/staging/
- stg_customers
- stg_products
- stg_orders
- stg_order_items

models/marts/
- dim_customer
- dim_product
- dim_date
- fact_sales

models/analytics/
- monthly_revenue
```

## Example Commands

```bash
dbt debug
dbt run
dbt test
dbt docs generate
```

Snowflake credentials are configured through environment variables in `profiles.yml.example`.