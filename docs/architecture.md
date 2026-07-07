# Architecture

This project implements a retail analytics platform using a medallion architecture in Snowflake. Raw retail CSV data is loaded into the Bronze layer, cleaned and standardized in the Silver layer, and modeled into analytics-ready Gold tables.

```mermaid
flowchart TD
    A[CSV Source Files] --> B[Bronze Raw Tables]
    B --> C[Silver Clean Tables]
    C --> D[Gold Star Schema]
    D --> E[Analytics SQL and Data Quality Tests] 