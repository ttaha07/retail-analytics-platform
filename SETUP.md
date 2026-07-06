# Setup Guide

This guide explains how to run the Retail Analytics Platform locally using Snowflake, Python, pytest, sample data, and visualization scripts.

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

## 5. Generate Sample Data

This repository includes a small synthetic sample dataset for local testing and demonstration.

Run:

```bash
python scripts/generate_sample_data.py
```

This creates sample CSV files under:

```text
data/sample/
```

Generated files:

```text
olist_customers_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_order_items_dataset.csv
```

These files match the naming expected by the Bronze ingestion scripts.

---

## 6. Create Visualizations

This project includes a basic visualization layer for demonstration and reporting.

Run:

```bash
python scripts/create_visualizations.py
```

This creates:

```text
visualizations/monthly_revenue.png
visualizations/revenue_by_category.png
visualizations/revenue_by_city.png
```

The charts demonstrate how curated data can support downstream analytics and BI reporting.

---

## 7. Upload Source CSV Files to Snowflake Stage

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

For local testing, you can generate the sample CSV files using:

```bash
python scripts/generate_sample_data.py
```

Then upload the generated files from:

```text
data/sample/
```

to the Snowflake internal stage used by `sql/bronze/load_data.sql`.

---

## 8. Run the Pipeline

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

## 9. Run Data Quality Tests

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

---

## 10. Optional: Airflow DAG

This project includes an optional Apache Airflow DAG to demonstrate scheduling, retries, task dependencies, and orchestration design.

The DAG file is located at:

```text
airflow/dags/retail_analytics_pipeline_dag.py
```

The DAG runs the following task flow:

```text
generate_sample_data
    -> run_snowflake_pipeline
    -> run_data_quality_tests
    -> create_visualizations
```

The DAG includes retry handling:

```text
retries: 2
retry_delay: 5 minutes
schedule: daily
catchup: false
```

The Airflow DAG is optional. The project can still be run directly using:

```bash
python orchestration/pipeline.py
```

---

## 11. GitHub Actions Setup

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

For more details on CI/CD configuration, see [CI_CD.md](CI_CD.md).

Go to:

```text
GitHub Repository -> Settings -> Secrets and variables -> Actions -> New repository secret
```

Forked repositories must configure their own Snowflake secrets before the workflow can run successfully.

---

## 12. Expected Validation Result

A successful pipeline run should show:

```text
Snowflake pipeline completed successfully.
```

A successful pytest run should show passing tests, for example:

```text
19 passed
```

The exact number of tests may change as the project evolves.

A successful visualization run should create:

```text
visualizations/monthly_revenue.png
```

---

## 13. Troubleshooting

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

### Visualization script fails

Confirm that sample data exists first.

Run:

```bash
python scripts/generate_sample_data.py
```

Then re-run:

```bash
python scripts/create_visualizations.py
```

---

## Optional dbt Setup

This project includes an optional dbt analytics engineering layer located in:

```text
dbt/retail_analytics/
```

Install the optional dbt dependencies:

```bash
pip install -r requirements-dbt.txt
```

Then move into the dbt project folder:

```bash
cd dbt/retail_analytics
```

Run dbt checks and models:

```bash
dbt debug
dbt run
dbt test
dbt docs generate
```

The dbt layer is optional and does not replace the main Snowflake SQL pipeline.

---


## Notes

This project uses live Snowflake execution. A Snowflake account and valid credentials are required to fully run the pipeline and tests.

The sample data generator and visualization script can be run locally without connecting to Snowflake.