
      begin;
    merge into "RAW"."SNAPSHOTS"."SNP_JHU_DASHBOARD_COVID_19_GLOBAL" as DBT_INTERNAL_DEST
    using "RAW"."SNAPSHOTS"."SNP_JHU_DASHBOARD_COVID_19_GLOBAL__dbt_tmp" as DBT_INTERNAL_SOURCE
    on DBT_INTERNAL_SOURCE.dbt_scd_id = DBT_INTERNAL_DEST.dbt_scd_id

    when matched
     and DBT_INTERNAL_DEST.dbt_valid_to is null
     and DBT_INTERNAL_SOURCE.dbt_change_type in ('update', 'delete')
        then update
        set dbt_valid_to = DBT_INTERNAL_SOURCE.dbt_valid_to

    when not matched
     and DBT_INTERNAL_SOURCE.dbt_change_type = 'insert'
        then insert ("COUNTRY_REGION", "PROVINCE_STATE", "COUNTY", "FIPS", "DATE", "ACTIVE", "PEOPLE_TESTED", "CONFIRMED", "PEOPLE_HOSPITALIZED", "DEATHS", "RECOVERED", "INCIDENT_RATE", "TESTING_RATE", "HOSPITALIZATION_RATE", "LONG", "LAT", "ISO3166_1", "ISO3166_2", "LAST_UPDATE_DATE", "DBT_UPDATED_AT", "DBT_VALID_FROM", "DBT_VALID_TO", "DBT_SCD_ID")
        values ("COUNTRY_REGION", "PROVINCE_STATE", "COUNTY", "FIPS", "DATE", "ACTIVE", "PEOPLE_TESTED", "CONFIRMED", "PEOPLE_HOSPITALIZED", "DEATHS", "RECOVERED", "INCIDENT_RATE", "TESTING_RATE", "HOSPITALIZATION_RATE", "LONG", "LAT", "ISO3166_1", "ISO3166_2", "LAST_UPDATE_DATE", "DBT_UPDATED_AT", "DBT_VALID_FROM", "DBT_VALID_TO", "DBT_SCD_ID")

;
    commit;
  