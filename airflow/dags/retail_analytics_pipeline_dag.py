from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


DEFAULT_ARGS = {
    "owner": "taha",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": False,
    "email_on_retry": False,
}


with DAG(
    dag_id="retail_analytics_pipeline",
    description="Orchestrates the Retail Analytics Snowflake pipeline, data quality checks, and visualization layer.",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["snowflake", "data-engineering", "retail-analytics"],
) as dag:

    generate_sample_data = BashOperator(
        task_id="generate_sample_data",
        bash_command="python scripts/generate_sample_data.py",
    )

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

    (
        generate_sample_data
        >> run_snowflake_pipeline
        >> run_data_quality_tests
        >> create_visualizations
    )