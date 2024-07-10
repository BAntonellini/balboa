from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


def run_inform_success(context):
    print("run_inform_success")

def run_inform_failure(context):
    print("run_inform_failure")


default_args = {
    'owner': 'airflow',
    "description": "Sample dag bash operator",
    'email': 'amorera@datacoves.com',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="bash_printenv_dag",
    default_args=default_args,
    start_date = datetime(2024, 3, 1),
    catchup=False,
    tags=["version_4"],
    description="Sample python teams dag",
    schedule_interval="*/10 * * * *",
    on_success_callback=run_inform_success,
    on_failure_callback=run_inform_failure,
) as dag:

    task_main = BashOperator(
        task_id = "task_main",
        bash_command = "sleep 30 && echo \"===========| LOG_LEVEL: $LOG_LEVEL |==========\" && cls"
    )

    task_main
