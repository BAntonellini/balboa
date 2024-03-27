import datetime

from airflow.decorators import dag
from operators.datacoves.dbt import DatacovesDbtOperator

@dag(
    default_args={
        "start_date": datetime.datetime(2024, 3, 27, 0, 0),
        "owner": "Alejandro Morera",
        "email": "alejandro@datacoves.com",
        "email_on_failure": True,
    },
    description="Sample DAG for dbt build",
    schedule_interval="0 0 1 */12 *",
    tags=["version_1"],
    catchup=False,
)
def yaml_dbt_dag():
    run_dbt = DatacovesDbtOperator(
        task_id="run_dbt",
        # bash_command="dbt run -s personal_loans"
        bash_command="dbt debug"
    )

dag = yaml_dbt_dag()
