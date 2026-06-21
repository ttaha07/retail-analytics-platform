# sql/bronze/run_bronze.py

import snowflake.connector
import os

conn = snowflake.connector.connect(
    user=os.environ["SNOWFLAKE_USER"],
    password=os.environ["SNOWFLAKE_PASSWORD"],
    account=os.environ["SNOWFLAKE_ACCOUNT"],
    warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
    database=os.environ["SNOWFLAKE_DATABASE"],
    schema=os.environ["SNOWFLAKE_SCHEMA"]
)

cur = conn.cursor()

print("Running Bronze Layer...")

sql_files = [
    "sql/bronze/create_tables.sql",
    "sql/bronze/load_data.sql",
    "sql/bronze/validation.sql"
]

for file in sql_files:
    with open(file, "r") as f:
        query = f.read()
        cur.execute(query)
        print(f"Executed {file}")

print("Bronze Complete")