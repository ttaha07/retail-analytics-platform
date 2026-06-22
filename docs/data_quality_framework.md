# Data Quality Framework

## Purpose

This framework validates data quality across the Retail Analytics Platform before analytics are trusted by business users.

## Checks Implemented

### 1. Null Checks

Validates that critical fields are not missing.

Fields checked:

- ORDER_ID
- CUSTOMER_ID
- PRODUCT_ID
- PRICE
- FREIGHT_VALUE

### 2. Duplicate Checks

Detects duplicate records in the fact table.

### 3. Row Count Validation

Compares record counts across Bronze, Silver, and Gold layers.

### 4. Freshness Checks

Validates the date range of the fact table and identifies the latest available order timestamp.

### 5. Referential Integrity Checks

Ensures fact table records match valid dimension table records.

## Why This Matters

Data pipelines can fail silently. Data quality checks help detect:

- Missing source data
- Broken joins
- Failed transformations
- Duplicate records
- Stale data
- Incorrect business metrics

## Interview Talking Point

I implemented a data quality framework that validates completeness, uniqueness, freshness, reconciliation, and referential integrity across the Medallion Architecture. This ensures the Gold layer can be trusted for business reporting.