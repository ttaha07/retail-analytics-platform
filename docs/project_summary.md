# Project Summary

## Project Name

Retail Analytics Platform

## Objective

Build an end-to-end Snowflake Data Engineering project that ingests raw retail data, transforms it through Bronze, Silver, and Gold layers, validates data quality, and generates business analytics.

## Architecture

The project follows a Medallion Architecture:

- Bronze: Raw source data
- Silver: Cleaned and standardized data
- Gold: Business-ready dimensional models

## Key Deliverables

- Snowflake database and schemas
- Internal stage and file format
- Bronze ingestion tables
- Silver cleaned tables
- Gold fact and dimension tables
- Analytics KPI queries
- Data quality framework
- Pipeline monitoring SQL
- GitHub documentation

## Business KPIs

- Total Revenue
- Monthly Revenue
- Top Products
- Customer Lifetime Value
- Regional Sales
- Top Customers

## Data Quality Checks

- Null checks
- Duplicate checks
- Row count validation
- Freshness checks
- Referential integrity checks

## Monitoring Checks

- Pipeline health check
- Table load summary
- Business KPI summary

## Interview Pitch

I built a Snowflake-based Retail Analytics Platform following Medallion Architecture. I loaded raw e-commerce data into Bronze tables, transformed and standardized data into Silver tables, modeled the Gold layer using fact and dimension tables, created analytics KPIs, implemented data quality validation, and added monitoring queries to validate pipeline health.