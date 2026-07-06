with customer_deduped as (
    select
        customer_id,
        customer_unique_id,
        customer_city,
        customer_state,
        row_number() over (
            partition by customer_unique_id
            order by customer_id
        ) as row_num
    from {{ ref('stg_customers') }}
)

select
    row_number() over (order by customer_unique_id) as customer_sk,
    customer_unique_id,
    customer_id as representative_customer_id,
    customer_city,
    customer_state,
    current_timestamp() as load_timestamp
from customer_deduped
where row_num = 1