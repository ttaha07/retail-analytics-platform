# Retail Analytics Platform

An end-to-end Data Engineering project built with Snowflake using a Medallion Architecture (Bronze, Silver, Gold).

## Features

- Snowflake Data Warehouse
- Internal Stages
- COPY INTO Data Loading
- Data Quality Validation
- Bronze / Silver / Gold Architecture
- Star Schema Modeling
- Revenue Analytics
- GitHub Version Control

## Tech Stack

- Snowflake
- SQL
- GitHub
- VS Code / Codespaces


## Architecture

![Architecture](screenshots/architecture_diagram.png)

Data flows through a Medallion Architecture:

CSV Files → Snowflake Stage → Bronze → Silver → Gold → Analytics

---

## Data Ingestion

Raw CSV files are uploaded into a Snowflake internal stage before being loaded into Bronze tables.

![Stage Files](screenshots/day2_stage_files.png)

---

## Bronze Layer

Raw source data is loaded into Bronze tables using Snowflake COPY INTO commands.

![Bronze Validation](screenshots/day2_bronze_row_counts.png)

---

## Silver Layer

The Silver layer performs cleansing, standardization, and deduplication of source data.

![Silver Tables](screenshots/day3_silver_tables.png)

---

## Gold Layer

Dimensional modeling was implemented using a star schema consisting of fact and dimension tables.

![Gold Tables](screenshots/day4_gold_tables.png)

---

## Revenue Analysis

The Gold layer supports business reporting and KPI generation.

![Revenue KPI](screenshots/day4_total_revenue.png)

# Retail Sales Data Pipeline

A production-style Data Engineering project implementing the Medallion Architecture.

## Features

- Bronze Layer (Raw Data)
- Silver Layer (Cleaned Data)
- Gold Layer (Business Metrics)
- Data Quality Testing
- Pipeline Orchestration
- GitHub Actions CI/CD

## Architecture

![Architecture](screenshots/day5_architecture_final.png)

## Screenshots

### Stage Files
![Stage Files](screenshots/day2_stage_files.png)

### Bronze Validation
![Bronze Validation](screenshots/day2_bronze_row_counts.png)

### Silver Layer
![Silver](screenshots/day3_silver_tables.png)

### Gold Layer
![Gold](screenshots/day4_gold_tables.png)

### Revenue Metrics
![Revenue](screenshots/day4_total_revenue.png)

### Architecture
![Architecture](screenshots/day5_architecture_final.png)

## Technologies Used

- Python
- Pandas
- Snowflake
- SQL
- Git
- GitHub Actions
- Medallion Architecture
- ETL Pipelines
- Data Quality Validation
