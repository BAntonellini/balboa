import datetime
import inspect

from airflow.decorators import dag
from operators.datacoves.dbt import DatacovesDbtOperator


@dag(
    default_args={
        "start_date": datetime.datetime(2023, 1, 1, 0, 0),
        "owner": "Noel Gomez",
        "email": "gomezn@example.com",
        "email_on_failure": True,
    },
    description="Sample DAG for dbt build",
    schedule_interval="0 0 1 */12 *",
    tags=["version_3"],
    catchup=False,
)
def yaml_dbt_dag():
    run_dbt = DatacovesDbtOperator(
        task_id="run_dbt", bash_command=inspect.cleandoc("""
        dbt run -s personal_loans && \
        curl -X POST $DATACOVES__UPLOAD_MANIFEST_URL \
        -H "Authorization: Bearer $DATACOVES__UPLOAD_MANIFEST_TOKEN" \
        -F "environment_slug=$DATACOVES__ENVIRONMENT_SLUG" \
        -F "run_id=$AIRFLOW_CTX_DAG_RUN_ID" \
        -F "file=@target/manifest.json" \
        --max-time 10
        """)
    )



dag = yaml_dbt_dag()
