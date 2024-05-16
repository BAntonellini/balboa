from airflow.decorators import dag
from operators.datacoves.data_sync import DatacovesDataSyncOperatorRedshift


@dag(
    default_args={"start_date": "2021-01"},
    description="sync_entire_db",
    schedule_interval="0 0 1 */12 *",
    tags=["version_1"],
    catchup=False,
)
def redshift_sync_airflow_db():
    # service connection name default is 'airflow_db_load'.
    # Destination type default is 'Redshift' (and the only one supported for now)
    sync_entire_db = DatacovesDataSyncOperatorRedshift(service_connection_name="main")


dag = redshift_sync_airflow_db()