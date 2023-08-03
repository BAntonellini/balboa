from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from callbacks.slack_messages import inform_success, inform_success

DATACOVES_INTEGRATION_NAME = "SLACK_TEST_01"


def run_inform_success(context):
    inform_success(
        context,
        connection_id=DATACOVES_INTEGRATION_NAME,  # Only mandatory argument
        # message="Custom python success message",
        # color="FFFF00",
    )

def run_inform_failure(context):
    inform_failure(
        context,
        connection_id=DATACOVES_INTEGRATION_NAME,  # Only mandatory argument
        # message="Custom python failure message",
        # color="FF00FF",
    )

default_args = {
    'owner': 'airflow',
    'email': 'some_user@example.com',
    'email_on_failure': True,
    'description': "Sample python dag with MS Teams notification",
}

with DAG(
    dag_id="mariano_test_01",
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["version_02"],
    description="Sample python dag dbt run",
    schedule_interval="0 0 1 */12 *",
    on_success_callback=run_inform_success,
    on_failure_callback=run_inform_failure,
) as dag:

    for i in range(10):
        successful_task = BashOperator(
            task_id = "successful_task_{i}",
            bash_command = "echo SUCCESS"
        )



    # failing_task = BashOperator(
    #     task_id = "failing_task",
    #     bash_command = "some_non_existant_command"
    # )

    # runs failing task
    # successful_task >> failing_task

    successful_task
