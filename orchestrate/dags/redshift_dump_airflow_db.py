from airflow.decorators import dag
from operators.datacoves.data_sync import DatacovesDataSyncOperatorRedshift


@dag(
    default_args={"start_date": "2021-01"},
    description="sync_entire_db",
    schedule_interval="0 0 1 */12 *",
    tags=["version_3"],
    catchup=False,
)
def redshift_sync_airflow_db():
    sync_entire_db = DatacovesDataSyncOperatorRedshift(
        service_connection_name="redshift", additional_tables=["log", "log_template"]
    )


dag = redshift_sync_airflow_db()
