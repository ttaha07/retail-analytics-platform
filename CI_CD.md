# CI/CD Guide

This project uses GitHub Actions to validate the Snowflake data pipeline and data quality test suite.

The workflow is defined in:

```text
.github/workflows/pipeline.yml
```

---

## What the Workflow Does

The CI/CD workflow runs whenever code is pushed to the repository or a pull request is opened.

The workflow performs the following steps:

```text
1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Runs the Snowflake pipeline
5. Runs pytest data quality checks
```

---

## Required GitHub Secrets

The workflow connects to Snowflake using GitHub repository secrets.

The following secrets are required:

```text
SNOWFLAKE_ACCOUNT
SNOWFLAKE_USER
SNOWFLAKE_PASSWORD
SNOWFLAKE_WAREHOUSE
SNOWFLAKE_DATABASE
SNOWFLAKE_SCHEMA
```

These values should never be hardcoded in the repository.

---

## How to Add Secrets in GitHub

Go to:

```text
Repository -> Settings -> Secrets and variables -> Actions -> New repository secret
```

Add each Snowflake value as a separate repository secret.

Example:

```text
Name: SNOWFLAKE_WAREHOUSE
Value: RETAIL_WH
```

---

## Local vs GitHub Actions Credentials

Local execution uses terminal environment variables:

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

GitHub Actions uses repository secrets:

```yaml
env:
  SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
  SNOWFLAKE_USER: ${{ secrets.SNOWFLAKE_USER }}
  SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}
  SNOWFLAKE_WAREHOUSE: ${{ secrets.SNOWFLAKE_WAREHOUSE }}
  SNOWFLAKE_DATABASE: ${{ secrets.SNOWFLAKE_DATABASE }}
  SNOWFLAKE_SCHEMA: ${{ secrets.SNOWFLAKE_SCHEMA }}
```

---

## Failure Handling

If the pipeline fails, GitHub Actions stops the workflow and reports the failed step.

The Python orchestration script provides details including:

```text
- SQL file that failed
- Statement number inside the file
- Preview of the failed SQL statement
- Original Snowflake error
```

This helps identify whether the issue came from:

```text
- Missing Snowflake credentials
- Missing staged CSV files
- SQL syntax issues
- Incorrect table or schema names
- Data quality validation failures
```

---

## Common CI/CD Failures

### Missing GitHub Secret

If a required secret is missing, the workflow will fail before connecting to Snowflake.

Check that all required secrets exist under repository settings.

---

### Snowflake Authentication Failure

If authentication fails, confirm:

```text
SNOWFLAKE_ACCOUNT
SNOWFLAKE_USER
SNOWFLAKE_PASSWORD
```

are correct.

---

### Missing Source Files in Stage

If `COPY INTO` fails, confirm that the required CSV files exist in the Snowflake internal stage.

Required files:

```text
olist_customers_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_order_items_dataset.csv
```

---

### Data Quality Test Failure

If pytest fails, review the failed assertion to identify the data quality rule that was violated.

Examples include:

```text
- Null primary business keys
- Missing surrogate keys
- Negative revenue values
- Failed referential integrity checks
- Empty fact or dimension tables
```

---

## Why This Matters

This CI/CD workflow demonstrates production-minded Data Engineering practices:

```text
- Automated pipeline validation
- Secret-based credential management
- Data quality testing
- Failure visibility
- Repeatable deployment checks
```