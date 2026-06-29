import pytest


pytestmark = pytest.mark.snowflake


def run_scalar_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result
    finally:
        cursor.close()


def run_scalar_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    return result


def test_fact_sales_has_rows(snowflake_connection):
    row_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES"
    )

    assert row_count > 0


def test_customer_dimension_has_rows(snowflake_connection):
    row_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.DIM_CUSTOMER"
    )

    assert row_count > 0


def test_product_dimension_has_rows(snowflake_connection):
    row_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.DIM_PRODUCT"
    )

    assert row_count > 0


def test_date_dimension_has_rows(snowflake_connection):
    row_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.DIM_DATE"
    )

    assert row_count > 0


def test_fact_sales_order_id_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE ORDER_ID IS NULL"
    )

    assert null_count == 0

def test_fact_sales_customer_unique_id_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE CUSTOMER_UNIQUE_ID IS NULL"
    )

    assert null_count == 0


def test_fact_sales_order_item_id_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE ORDER_ITEM_ID IS NULL"
    )

    assert null_count == 0


def test_fact_sales_customer_id_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE CUSTOMER_ID IS NULL"
    )

    assert null_count == 0


def test_fact_sales_product_id_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE PRODUCT_ID IS NULL"
    )

    assert null_count == 0


def test_fact_sales_order_date_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE ORDER_DATE IS NULL"
    )

    assert null_count == 0


def test_fact_sales_total_sale_amount_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE TOTAL_SALE_AMOUNT IS NULL"
    )

    assert null_count == 0


def test_fact_sales_total_sale_amount_not_negative(snowflake_connection):
    negative_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE TOTAL_SALE_AMOUNT < 0"
    )

    assert negative_count == 0


def test_fact_sales_sales_sk_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE SALES_SK IS NULL"
    )

    assert null_count == 0


def test_fact_sales_customer_sk_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE CUSTOMER_SK IS NULL"
    )

    assert null_count == 0


def test_fact_sales_product_sk_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE PRODUCT_SK IS NULL"
    )

    assert null_count == 0


def test_fact_sales_date_sk_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE DATE_SK IS NULL"
    )

    assert null_count == 0


def test_fact_sales_load_timestamp_not_null(snowflake_connection):
    null_count = run_scalar_query(
        snowflake_connection,
        "SELECT COUNT(*) FROM GOLD.FACT_SALES WHERE LOAD_TIMESTAMP IS NULL"
    )

    assert null_count == 0


def test_customer_referential_integrity(snowflake_connection):
    missing_customers = run_scalar_query(
        snowflake_connection,
        """
        SELECT COUNT(*)
        FROM GOLD.FACT_SALES fs
        LEFT JOIN GOLD.DIM_CUSTOMER dc
            ON fs.CUSTOMER_SK = dc.CUSTOMER_SK
        WHERE dc.CUSTOMER_SK IS NULL
        """
    )

    assert missing_customers == 0

def test_customer_unique_id_unique(snowflake_connection):
    duplicate_count = run_scalar_query(
        snowflake_connection,
        """
        SELECT COUNT(*)
        FROM (
            SELECT CUSTOMER_UNIQUE_ID
            FROM GOLD.DIM_CUSTOMER
            GROUP BY CUSTOMER_UNIQUE_ID
            HAVING COUNT(*) > 1
        )
        """
    )

    assert duplicate_count == 0


def test_product_referential_integrity(snowflake_connection):
    missing_products = run_scalar_query(
        snowflake_connection,
        """
        SELECT COUNT(*)
        FROM GOLD.FACT_SALES fs
        LEFT JOIN GOLD.DIM_PRODUCT dp
            ON fs.PRODUCT_SK = dp.PRODUCT_SK
        WHERE dp.PRODUCT_SK IS NULL
        """
    )

    assert missing_products == 0


def test_date_referential_integrity(snowflake_connection):
    missing_dates = run_scalar_query(
        snowflake_connection,
        """
        SELECT COUNT(*)
        FROM GOLD.FACT_SALES fs
        LEFT JOIN GOLD.DIM_DATE dd
            ON fs.DATE_SK = dd.DATE_SK
        WHERE dd.DATE_SK IS NULL
        """
    )

    assert missing_dates == 0