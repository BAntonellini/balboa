

with dbt_tests as (

    select * from 
    
        BALBOA.source_dbt_artifacts.stg_dbt__tests
    


),

run_results as (

    select *
    from 
    
        BALBOA.source_dbt_artifacts.fct_dbt__run_results
    


),

dbt_tests_incremental as (

    select dbt_tests.*
    from dbt_tests
    -- Inner join with run results to enforce consistency and avoid race conditions.
    -- https://github.com/brooklyn-data/dbt_artifacts/issues/75
    inner join run_results on
        dbt_tests.artifact_run_id = run_results.artifact_run_id

    
        -- this filter will only be applied on an incremental run
        where dbt_tests.artifact_generated_at > (select max(artifact_generated_at) from BALBOA.source_dbt_artifacts.dim_dbt__tests)
    

),

fields as (

    select
        manifest_test_id,
        command_invocation_id,
        dbt_cloud_run_id,
        artifact_run_id,
        artifact_generated_at,
        node_id,
        name,
        depends_on_nodes,
        package_name,
        test_path
    from dbt_tests_incremental

)

select * from fields