select distinct
    to_number(to_char(order_date, 'YYYYMMDD')) as date_sk,
    order_date,
    year(order_date) as order_year,
    month(order_date) as order_month,
    day(order_date) as order_day,
    dayofweek(order_date) as day_of_week,
    current_timestamp() as load_timestamp
from {{ ref('stg_orders') }}
where order_date is not null