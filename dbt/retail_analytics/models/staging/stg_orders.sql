select
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    cast(order_purchase_timestamp as date) as order_date
from {{ source('silver', 'SILVER_ORDERS') }}
where order_id is not null