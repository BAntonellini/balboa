from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy import DummyOperator
import logging
import time

logger = logging.getLogger(__name__)

default_args = {
    'owner': 'airflow',
    'description': "Sample python dag to check real time logs",
    'email': 'amorera@datacoves.com',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id = "real_time_logs",
    default_args = default_args,
    start_date = datetime(2024, 3, 1),
    catchup = False,
    tags = ["version_1"],
    description = "Sample python dag dbt run",
    schedule_interval="*/10 * * * *",
) as dag:

    @task(task_id="real_time_logs")
    def real_time_logs(**kwargs):
        for i in range(100):
            logger.info("Real time logs %s", i+1)
            time.sleep(2)

        return "real_time_logs finish"

    start_task = DummyOperator(task_id='start_task')
    end_task = DummyOperator(task_id='end_task')

    my_real_time_logs = real_time_logs()
    start_task >> my_real_time_logs >> end_task

    """
    for i in range(10):
        @task(task_id=f"sleep_for_{i+1}")
        def my_sleeping_function(random_base):
            t = random_base + 15
            return f"SLEEP {t}"
            time.sleep(t)

        sleeping_task = my_sleeping_function(random_base=i/10)
        my_print_context >> my_task_1 >> sleeping_task
    """
