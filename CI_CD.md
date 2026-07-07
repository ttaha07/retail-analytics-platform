# CI/CD Guide

This project uses GitHub Actions to validate the pipeline on every push and pull request to `main`.

The workflow is designed to prove that the project is reproducible, testable, and safe to run without exposing Snowflake credentials.

### Workflow Overview

| Step | What It Validates | Why It Matters |
|---|---|---|
| Checkout repository | Pulls the latest project code into the GitHub runner. | Ensures CI tests the exact version being committed. |
| Set up Python | Installs Python 3.12 with pip caching. | Keeps the runtime consistent and improves workflow speed. |
| Install dependencies | Installs Python packages from `requirements.txt`. | Confirms the project can be installed from a clean environment. |
| Compile Python files | Runs syntax checks against orchestration and test code. | Catches Python syntax errors before runtime. |
| Build Docker image | Builds the project container. | Confirms the pipeline can run in a portable Docker environment. |
| Run Snowflake pipeline | Executes the Snowflake orchestration script when secrets are available. | Validates the end-to-end Snowflake pipeline in CI. |
| Run data quality checks | Runs `pytest` against Gold-layer Snowflake tables. | Confirms the curated analytics layer passes quality checks. |
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