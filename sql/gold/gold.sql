# sql/gold/run_gold.py

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

print("Running Gold Layer...")

files = [
    "sql/gold/create_fact_table.sql",
    "sql/gold/create_dimensions.sql",
    "sql/gold/validation.sql"
]

for fpath in files:
    with open(fpath, "r") as f:
        cur.execute(f.read())
        print(f"Executed {fpath}")

print("Gold Complete")