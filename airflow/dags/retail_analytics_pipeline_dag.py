from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="retail_analytics_pipeline",
    default_args=default_args,
    description="Orchestrates the Retail Analytics Snowflake pipeline.",
    schedule_interval=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["snowflake", "retail", "data-engineering"],
) as dag:
    run_snowflake_pipeline = BashOperator(
        task_id="run_snowflake_pipeline",
        bash_command="python orchestration/pipeline.py",
    )

    run_data_quality_tests = BashOperator(
        task_id="run_data_quality_tests",
        bash_command="pytest tests/data_quality_checks.py -v",
    )

    create_visualizations = BashOperator(
        task_id="create_visualizations",
        bash_command="python scripts/create_visualizations.py",
    )

    run_snowflake_pipeline >> run_data_quality_tests >> create_visualizations