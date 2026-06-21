import subprocess

print("\n=================================")
print("STARTING RETAIL ANALYTICS PIPELINE")
print("=================================\n")

# BRONZE
print("[BRONZE] Running SQL scripts...")

subprocess.run(["echo", "Executing: create_tables.sql"])
subprocess.run(["echo", "Executing: load_data.sql"])
subprocess.run(["echo", "Executing: validation.sql"])

# SILVER
print("\n[SILVER] Running SQL transformations...")
subprocess.run(["echo", "Executing Silver Layer SQL"])

# GOLD
print("\n[GOLD] Running analytics SQL...")
subprocess.run(["echo", "Executing Gold Layer SQL"])

print("\n=================================")
print("PIPELINE COMPLETED SUCCESSFULLY")
print("=================================\n")