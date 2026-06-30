# Setup Guide

This guide explains how to run the Retail Analytics Platform locally using Snowflake, Python, and pytest.

---

## Prerequisites

Before running this project, you need:

- A Snowflake account
- A Snowflake warehouse
- Python 3.12 or later
- Git
- Snowflake credentials configured as environment variables

---

## 1. Clone the Repository

```bash
git clone https://github.com/ttaha07/retail-analytics-platform.git
cd retail-analytics-platform
```

---

## 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Snowflake Objects Required

The pipeline expects the following Snowflake objects:

```text
Warehouse: RETAIL_WH
Database: RETAIL_ANALYTICS_DB

Schemas:
- BRONZE
- SILVER
- GOLD
```

The SQL scripts in the `sql/` folder create and rebuild the required tables.

---

## 4. Configure Snowflake Environment Variables

Set the following environment variables in your terminal:

```bash
export SNOWFLAKE_ACCOUNT="your_snowflake_account"
export SNOWFLAKE_USER="your_snowflake_username"
export SNOWFLAKE_WAREHOUSE="RETAIL_WH"
export SNOWFLAKE_DATABASE="RETAIL_ANALYTICS_DB"
export SNOWFLAKE_SCHEMA="GOLD"

read -s -p "Snowflake password: " SNOWFLAKE_PASSWORD
export SNOWFLAKE_PASSWORD
echo
```

Do not hardcode Snowflake credentials in project files.

---

## 5. Upload Source CSV Files to Snowflake Stage

The Bronze load scripts expect these source files to exist in the Snowflake internal stage:

```text
olist_customers_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_order_items_dataset.csv
```

Expected source-to-table mapping:

```text
olist_customers_dataset.csv      -> BRONZE_CUSTOMERS
olist_orders_dataset.csv         -> BRONZE_ORDERS
olist_products_dataset.csv       -> BRONZE_PRODUCTS
olist_order_items_dataset.csv    -> BRONZE_ORDER_ITEMS
```

The stage and file format are created by the Bronze SQL scripts.

---

## 6. Run the Pipeline

Run the Python orchestration script:

```bash
python orchestration/pipeline.py
```

The pipeline runs SQL files in dependency order:

```text
Bronze creation and loading
Silver cleansing and deduplication
Gold star schema creation
Business analytics queries
Data quality checks
Pipeline monitoring checks
```

If a SQL statement fails, the pipeline raises an error showing:

- The SQL file that failed
- The statement number inside the file
- A preview of the failed SQL statement
- The original Snowflake error

---

## 7. Run Data Quality Tests

Run the pytest validation suite:

```bash
pytest tests/data_quality_checks.py -v
```

These tests validate:

- Fact table row counts
- Dimension table row counts
- Surrogate keys
- Required non-null fields
- Revenue values
- Load timestamps
- Customer, product, and date referential integrity

---

## 8. GitHub Actions Setup

The GitHub Actions workflow requires Snowflake credentials to be stored as repository secrets.

Add these secrets in GitHub:

```text
SNOWFLAKE_ACCOUNT
SNOWFLAKE_USER
SNOWFLAKE_PASSWORD
SNOWFLAKE_WAREHOUSE
SNOWFLAKE_DATABASE
SNOWFLAKE_SCHEMA
```

Go to:

```text
GitHub Repository -> Settings -> Secrets and variables -> Actions -> New repository secret
```

Forked repositories must configure their own Snowflake secrets before the workflow can run successfully.

---

## 9. Expected Validation Result

A successful pipeline run should show:

```text
Snowflake pipeline completed successfully.
```

A successful pytest run should show passing tests, for example:

```text
19 passed
```

The exact number of tests may change as the project evolves.

---

## 10. Troubleshooting

### Tests are skipped

If pytest shows skipped tests, Snowflake credentials are not configured in your terminal session.

Re-run the environment variable export commands.

### Pipeline fails on a SQL file

The pipeline error message will show:

- The SQL file that failed
- The statement number
- A preview of the failed SQL
- The original Snowflake error

Use that information to debug the failing SQL script.

### GitHub Actions fails

Check that all required Snowflake secrets are configured in the repository settings.

### COPY INTO fails

Confirm that the expected CSV files exist in the Snowflake internal stage and that the file names match the paths in `sql/bronze/load_data.sql`.

---

## Notes

This project uses live Snowflake execution. A Snowflake account and valid credentials are required to fully run the pipeline and tests.