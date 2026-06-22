# Architecture

The platform follows a Medallion Architecture (Bronze → Silver → Gold).

![Architecture](screenshots/day5_architecture_final.png)

# Data Ingestion

Raw CSV files are loaded into Snowflake Internal Stages and ingested using COPY INTO commands.

![Stage Files](screenshots/day2_stage_files.png)

# Bronze Layer

The Bronze Layer stores raw source data exactly as received from source systems.

![Bronze Validation](screenshots/day2_bronze_row_counts.png)

# Silver Layer

The Silver Layer performs data cleansing, standardization, and validation.

![Silver Tables](screenshots/day3_silver_tables.png)

### Duplicate Validation

Duplicate detection is performed to ensure data quality before loading analytics layers.

![Duplicate Validation](screenshots/day3_order_duplicate_check.png)

# Gold Layer

The Gold Layer contains dimensional models optimized for business reporting.

Implemented:

- FACT_SALES
- DIM_CUSTOMER
- DIM_PRODUCT
- DIM_DATE

![Gold Tables](screenshots/day4_gold_tables.png)

# Revenue Analysis

The platform supports business KPI generation.

### Total Revenue

![Revenue KPI](screenshots/day4_total_revenue.png)

### Monthly Revenue Trend

![Monthly Revenue](screenshots/day5_monthly_revenue.png)

### Top Products

![Top Products](screenshots/day5_top_products.png)

# Data Quality Framework

The project includes automated validation checks to improve trust in reporting.

![Data Quality](screenshots/day5_data_quality_checks.png)

### Data Quality Summary

![Data Quality Summary](screenshots/day6_data_quality_summary.png)

### Row Count Validation

![Row Count Validation](screenshots/day6_row_count_validation.png)

### Null Value Validation

![Null Checks](screenshots/day6_null_checks.png)

### Duplicate Detection

![Duplicate Checks](screenshots/day6_duplicate_checks.png)

### Freshness Validation

![Freshness Checks](screenshots/day6_freshness_checks.png)

### Referential Integrity Validation

![Referential Integrity Checks](screenshots/day6_referential_integrity_checks.png)

# Pipeline Monitoring

Monitoring validates operational health of the analytics platform.

### Pipeline Health Check

![Pipeline Health Check](screenshots/day7_pipeline_health_check.png)

### Table Load Summary

![Table Load Summary](screenshots/day7_table_load_summary.png)

### Business KPI Summary

![Business KPI Summary](screenshots/day7_business_kpi_summary.png)

# Skills Demonstrated

- Snowflake
- SQL
- Data Warehousing
- ETL / ELT
- Medallion Architecture
- Star Schema Modeling
- Data Quality Validation
- Pipeline Monitoring
- GitHub Actions CI/CD