import os
from pathlib import Path

import snowflake.connector


SQL_FILES = [
    # Bronze layer
    "sql/bronze/create_tables.sql",
    "sql/bronze/load_data.sql",
    "sql/bronze/validation.sql",

    # Silver layer
    "sql/silver/create_silver_tables.sql",
    "sql/silver/load_silver_tables.sql",
    "sql/silver/validation.sql",

    # Gold layer
    "sql/gold/create_dimensions.sql",
    "sql/gold/create_fact_table.sql",
    "sql/gold/validation.sql",

    # Analytics layer
    "sql/analytics/revenue.sql",
    "sql/analytics/monthly_revenue.sql",
    "sql/analytics/top_products.sql",
    "sql/analytics/customer_lifetime_value.sql",
    "sql/analytics/customer_retention.sql",
    "sql/analytics/regional_sales.sql",
    "sql/analytics/validation.sql",

    # Data quality checks
    "sql/data_quality/null_checks.sql",
    "sql/data_quality/duplicate_checks.sql",
    "sql/data_quality/freshness_checks.sql",
    "sql/data_quality/referential_integrity_checks.sql",
    "sql/data_quality/row_count_validation.sql",
    "sql/data_quality/data_quality_summary.sql",

    # Monitoring checks
    "sql/monitoring/pipeline_health_check.sql",
    "sql/monitoring/table_load_summary.sql",
    "sql/monitoring/business_kpi_summary.sql",
]


REQUIRED_ENV_VARS = [
    "SNOWFLAKE_ACCOUNT",
    "SNOWFLAKE_USER",
    "SNOWFLAKE_PASSWORD",
    "SNOWFLAKE_WAREHOUSE",
    "SNOWFLAKE_DATABASE",
    "SNOWFLAKE_SCHEMA",
]


def get_connection():
    missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]

    if missing_vars:
        raise EnvironmentError(
            f"Missing required Snowflake environment variables: {', '.join(missing_vars)}"
        )

    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )


def execute_sql_file(cursor, file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"SQL file not found: {file_path}")

    sql_text = path.read_text()

    print(f"Running: {file_path}")

    statements = [stmt.strip() for stmt in sql_text.split(";") if stmt.strip()]

    for statement in statements:
        cursor.execute(statement)

    print(f"Completed: {file_path}")


def run_pipeline():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        for sql_file in SQL_FILES:
            execute_sql_file(cursor, sql_file)

        print("Snowflake pipeline completed successfully.")

    finally:
        connection.close()


if __name__ == "__main__":
    run_pipeline()