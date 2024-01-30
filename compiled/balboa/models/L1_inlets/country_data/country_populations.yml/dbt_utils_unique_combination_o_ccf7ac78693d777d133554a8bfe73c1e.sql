





with validation_errors as (

    select
        country_code, year
    from balboa.l1_country_data.country_populations
    group by country_code, year
    having count(*) > 1

)

select *
from validation_errors


