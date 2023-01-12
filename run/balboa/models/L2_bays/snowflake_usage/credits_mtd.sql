
  create or replace  view BALBOA_STAGING.l2_snowflake_usage.credits_mtd
  
    
    
(
  
    "MTD_CREDITS_USED" COMMENT $$$$, 
  
    "PREVIOUS_MTD_CREDITS_USED" COMMENT $$$$
  
)

  copy grants as (
    select
    credits_used as mtd_credits_used,
    (
        select sum(credits_used) as credits_used_sum
        from
            l2_snowflake_usage.int_warehouse_metering_history
        where
            timestampdiff(month, start_time, current_date) = 1
            and day(current_date) >= day(start_time)
    ) as previous_mtd_credits_used
from
    l2_snowflake_usage.int_warehouse_metering_history
where
    timestampdiff(month, start_time, current_date) = 0
  );