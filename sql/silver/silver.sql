# sql/silver/run_silver.py

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

print("Running Silver Layer...")

files = [
    "sql/silver/create_silver_tables.sql",
    "sql/silver/load_silver_tables.sql",
    "sql/silver/validation.sql"
]

for fpath in files:
    with open(fpath, "r") as f:
        cur.execute(f.read())
        print(f"Executed {fpath}")

print("Silver Complete")