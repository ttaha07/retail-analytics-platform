import os

import pytest
import snowflake.connector


REQUIRED_ENV_VARS = [
    "SNOWFLAKE_ACCOUNT",
    "SNOWFLAKE_USER",
    "SNOWFLAKE_PASSWORD",
    "SNOWFLAKE_WAREHOUSE",
    "SNOWFLAKE_DATABASE",
    "SNOWFLAKE_SCHEMA",
]


def snowflake_config_available():
    return all(os.getenv(var) for var in REQUIRED_ENV_VARS)


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "snowflake: marks tests that require live Snowflake credentials"
    )


def pytest_collection_modifyitems(config, items):
    if snowflake_config_available():
        return

    skip_snowflake = pytest.mark.skip(
        reason="Snowflake credentials not configured."
    )

    for item in items:
        if "snowflake" in item.keywords:
            item.add_marker(skip_snowflake)


@pytest.fixture(scope="module")
def snowflake_connection():
    connection = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        login_timeout=30,
        network_timeout=60,
        socket_timeout=30,
    )

    yield connection

    connection.close()