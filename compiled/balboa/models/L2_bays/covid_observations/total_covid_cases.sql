with raw_cases as (
    select
        country_region,
        province_state,
        county,
        new_cases,
        date,
        case_type
    from balboa.l2_covid_observations.base_cases
),

create_location_id as (
    select
        md5(cast(coalesce(cast(country_region as TEXT), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(province_state as TEXT), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(county as TEXT), '_dbt_utils_surrogate_key_null_') as TEXT)) as location_id, --noqa
        new_cases,
        date,
        case_type
    from raw_cases
),

pivoted_model as (
    select
        location_id,
        date,
        sum("'Confirmed'") as confirmed,
        sum("'Deaths'") as deaths,
        sum("'Active'") as active,
        sum("'Recovered'") as recovered
    from create_location_id
    pivot (sum(new_cases) for case_type in ('Confirmed', 'Deaths', 'Active', 'Recovered')) as case_pivot
    group by location_id, date
)

select *
from pivoted_model