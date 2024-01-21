import datetime

from airflow.decorators import dag
from operators.datacoves.bash import DatacovesBashOperator


@dag(
    default_args={"start_date": "2021-01"},
    description="Loan Run",
    schedule_interval="0 0 1 */12 *",
    tags=["version_6"],
    catchup=False,
)
def daily_loan_run():
    transform = DatacovesBashOperator(
        task_id="transform",
        bash_command=" pwd && echo =========== && dbt-coves dbt -- ls -s awer -t prd' echo =========== && pwd",
    )
    extract_and_load_dlt = DatacovesBashOperator(
        task_id="extract_and_load_dlt",
        bash_command=" cd $DATACOVES__DBT_HOME && cd ../load/dlt/ && echo =========== && pwd && echo =========== && python csv_to_snowflake/load_csv_data.py && echo ===========",
    )
    extract_and_load_dlt.set_upstream([transform])


dag = daily_loan_run()
