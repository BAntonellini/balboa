import datetime

from airflow.decorators import dag
from operators.datacoves.dbt import DatacovesDbtOperator

@dag(
    default_args={
        "start_date": datetime.datetime(2024, 3, 27, 0, 0),
        "owner": "Alejandro Morera",
    },
    description="Sample DAG for dbt build",
    schedule_interval="0 0 1 */12 *",
    tags=["version_3"],
    catchup=False,
)
def dbt_command():
    run_dbt = DatacovesDbtOperator(
        task_id="run_dbt_commands",
        # bash_command="dbt run -s personal_loans"
        bash_command="dbt debug && dbt ls && dbt-coves dbt"
    )

dag = dbt_command()
