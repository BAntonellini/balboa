"""
DAG that is set to run manually if Environment slug matches gay725
"""

import datetime
import os

from airflow.decorators import dag
from operators.datacoves.dbt import DatacovesDbtOperator

schedule = (
    None
    if "gay725" in os.environ.get("DATACOVES__ENVIRONMENT_SLUG", "")
    else "0 0 1 */12 *"
)


@dag(
    default_args={
        "start_date": datetime.datetime(2023, 1, 1, 0, 0),
        "owner": "Noel Gomez",
        "email": "gomezn@example.com",
        "email_on_failure": True,
    },
    description="Sample DAG for dbt build",
    schedule_interval=schedule,
    tags=["version_1"],
    catchup=False,
)
def manual_gay725_run():
    dbt_list = DatacovesDbtOperator(task_id="dbt_list", bash_command="dbt ls")


dag = manual_gay725_run()
