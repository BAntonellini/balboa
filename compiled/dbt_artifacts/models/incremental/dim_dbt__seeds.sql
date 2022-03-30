

with dbt_seeds as (

    select * from 
    
        BALBOA.source_dbt_artifacts.stg_dbt__seeds
    


),

run_results as (

    select *
    from 
    
        BALBOA.source_dbt_artifacts.fct_dbt__run_results
    


),

dbt_seeds_incremental as (

    select dbt_seeds.*
    from dbt_seeds
    -- Inner join with run results to enforce consistency and avoid race conditions.
    -- https://github.com/brooklyn-data/dbt_artifacts/issues/75
    inner join run_results on
        dbt_seeds.artifact_run_id = run_results.artifact_run_id

    
        -- this filter will only be applied on an incremental run
        where dbt_seeds.artifact_generated_at > (select max(artifact_generated_at) from BALBOA.source_dbt_artifacts.dim_dbt__seeds)
    

),

fields as (

    select
        manifest_seed_id,
        command_invocation_id,
        dbt_cloud_run_id,
        artifact_run_id,
        artifact_generated_at,
        node_id,
        seed_database,
        seed_schema,
        name,
        depends_on_nodes,
        package_name,
        seed_path,
        checksum
    from dbt_seeds_incremental

)

select * from fields