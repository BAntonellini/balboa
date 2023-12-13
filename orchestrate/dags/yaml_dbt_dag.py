import datetime
import os
import subprocess

from airflow.decorators import dag
from operators.datacoves.bash import DatacovesBashOperator


@dag(
    default_args={
        "start_date": datetime.datetime(2023, 1, 1, 0, 0),
    },
    description="Sample DAG for dbt build",
    schedule_interval="0 0 1 */12 *",
    tags=["version_1"],
    catchup=False,
)
def yaml_dbt_dag():
    command = "source /opt/datacoves/virtualenvs/main/bin/activate && pip install git+https://github.com/datacoves/dbt-coves.git@optionally-upload-manifest-to-dbt-api dbt-snowflake"
    subprocess.run(command, shell=True, check=True, executable="/bin/bash", text=True)

    for name, value in os.environ.items():
        print(f"{name}: {value}")

    build_dbt = DatacovesBashOperator(
        task_id="build_dbt",
        bash_command="dbt-coves dbt -- run -s personal_loans",
    )


dag = yaml_dbt_dag()
