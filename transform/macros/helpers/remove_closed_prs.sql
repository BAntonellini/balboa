{# This macro receives a list of closed pr ids joined by commas, and removes any databases that still exist. #}
{#
    To run: 
    dbt run-operation remove_closed_prs --args '{pr_ids: 1|2|3|4|5}'
#}

{%- macro remove_closed_prs(pr_ids) -%}
  {% set pr_array = pr_ids.split("|") %}
  {% for this_pr in pr_array %}
    {% set this_db = 'BALBOA_PR_' ~ this_pr %}
    {{ log("Running drop statement for database: " ~ this_db, info=true) }}
    {% set drop_db_sql %}
        DROP DATABASE IF EXISTS {{ this_db }};
    {% endset %}
    {% do run_query(drop_db_sql) %}
  {% endfor %}
{%- endmacro -%}
