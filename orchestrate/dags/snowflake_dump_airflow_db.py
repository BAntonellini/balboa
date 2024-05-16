from airflow.decorators import dag
from operators.datacoves.data_sync import DatacovesDataSyncOperatorSnowflake


@dag(
    default_args={"start_date": "2021-01"},
    description="sync_data_script",
    schedule_interval="0 0 1 */12 *",
    tags=["version_1"],
    catchup=False,
)
def snowflake_sync_airflow_db():
    # service connection name default is 'airflow_db_load'.
    # Destination type default is 'snowflake' (and the only one supported for now)
    sync_entire_db = DatacovesDataSyncOperatorSnowflake()


dag = snowflake_sync_airflow_db()
