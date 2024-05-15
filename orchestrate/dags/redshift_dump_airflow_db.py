from airflow.decorators import dag
from operators.datacoves.data_sync import DatacovesDataSyncOperatorRedshift


@dag(
    default_args={"start_date": "2021-01"},
    description="sync_data_script",
    schedule_interval="0 0 1 */12 *",
    tags=["version_2"],
    catchup=False,
)
def sync_airflow_db_redshift():
    # service connection name default is 'airflow_db_load'.
    # Destination type default is 'Redshift' (and the only one supported for now)
    sync_data_script = DatacovesDataSyncOperatorRedshift()


dag = sync_airflow_db_redshift()
