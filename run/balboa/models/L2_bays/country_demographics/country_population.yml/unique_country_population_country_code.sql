select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
        select *
        from balboa_STAGING.dbt_test__audit.unique_country_population_country_code
    
      
    ) dbt_internal_test