import datetime

from airflow.decorators import dag, task
from notifiers.datacoves.ms_teams import MSTeamsNotifier


@dag(
    default_args={
        "start_date": datetime.datetime(2023, 1, 1, 0, 0),
        "owner": "Bruno Antonellini",
        "email": "bruno@datacoves.com",
        "email_on_failure": False,
    },
    description="Sample DAG for dbt build",
    schedule=None,
    tags=["version_1"],
    catchup=False,
    # on_success_callback=MSTeamsNotifier(message="DAG Succeeded"),
    # on_failure_callback=MSTeamsNotifier(message="DAG Failed"),
)
def new_notifier():
    @task(
        on_success_callback=MSTeamsNotifier(message="Success!"),
    )
    def t1():
        return "hello"

    t1()


dag = new_notifier()
