from airflow.decorators import dag
from operators.datacoves.data_sync import DatacovesDataSyncOperatorSnowflake


@dag(
    default_args={"start_date": "2021-01"},
    description="sync_some_tables_to_custom_schema",
    schedule_interval="0 0 1 */12 *",
    tags=["version_1"],
    catchup=False,
)
def snowflake_sync_airflow_tables():
    # service connection name default is 'airflow_db_load'.
    # Destination type default is 'snowflake' (and the only one supported for now)
    sync_some_tables_to_custom_schema = DatacovesDataSyncOperatorSnowflake(
        destination_schema="BRUNO_TABLES_DUMP",
        tables=["task_fail", "task_instance"],
    )


dag = snowflake_sync_airflow_tables()
