
  
    

        create or replace transient table BALBOA_STAGING.l3_covid_analytics.covid_cases_county copy grants as
        (with  __dbt__cte__covid_location as (


with jhu_covid_19 as (
    select distinct
        country_region,
        COALESCE(province_state, 'UNDEFINED') as province_state,
        COALESCE(county, 'UNDEFINED') as county,
        lat,
        long,
        iso3166_1,
        iso3166_2,
        date
    from BALBOA_STAGING.l1_starschema_covid19.jhu_covid_19
),

rank_locations as (
    select
        HASH(country_region || '|' || province_state || '|' || county) as snowflake_location_id,
        md5(cast(coalesce(cast(country_region as TEXT), '') || '-' || coalesce(cast(province_state as TEXT), '') || '-' || coalesce(cast(county as TEXT), '') as TEXT)) as location_id,
        country_region as country,
        province_state as state,
        county,
        lat,
        long,
        iso3166_1,
        iso3166_2,
        RANK() over (partition by location_id order by date desc) as rowrank
    from jhu_covid_19
)

select
    location_id,
    country,
    state,
    county,
    lat,
    long,
    iso3166_1,
    iso3166_2
from rank_locations
where rowrank = 1
),covid_cases as (
    select * from BALBOA_STAGING.l2_covid_observations.total_covid_cases
),

location as (
    select * from __dbt__cte__covid_location
)

select
    location.country,
    location.state,
    location.county,
    location.lat,
    location.long,
    cases.date,
    cases.confirmed,
    cases.deaths,
    cases.active,
    cases.recovered
from covid_cases as cases
left join location as location
    on location.location_id = cases.location_id
where location.county is not null
        );
      
  