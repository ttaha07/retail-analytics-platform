# Architecture

This project implements a Snowflake retail analytics platform using a medallion architecture. Raw CSV files are loaded into Bronze, cleaned in Silver, and modeled into Gold fact and dimension tables for analytics.

```mermaid
flowchart TD
    A[CSV Source Files] --> B[Bronze Raw Tables]
    B --> C[Silver Clean Tables]
    C --> D[Gold Star Schema]
    D --> E[Analytics SQL and Data Quality Tests]
```