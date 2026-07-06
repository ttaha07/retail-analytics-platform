with sales_base as (
    select
        oi.order_id,
        oi.order_item_id,
        oi.product_id,
        o.customer_id,
        c.customer_unique_id,
        o.order_purchase_timestamp,
        o.order_date,
        oi.price,
        oi.freight_value,
        oi.total_sale_amount
    from {{ ref('stg_order_items') }} oi
    inner join {{ ref('stg_orders') }} o
        on oi.order_id = o.order_id
    inner join {{ ref('stg_customers') }} c
        on o.customer_id = c.customer_id
)

select
    row_number() over (
        order by sb.order_id, sb.order_item_id
    ) as sales_sk,
    dc.customer_sk,
    dp.product_sk,
    dd.date_sk,
    sb.order_id,
    sb.order_item_id,
    sb.product_id,
    sb.customer_id,
    sb.customer_unique_id,
    sb.order_purchase_timestamp,
    sb.order_date,
    sb.price,
    sb.freight_value,
    sb.total_sale_amount,
    current_timestamp() as load_timestamp
from sales_base sb
inner join {{ ref('dim_customer') }} dc
    on sb.customer_unique_id = dc.customer_unique_id
inner join {{ ref('dim_product') }} dp
    on sb.product_id = dp.product_id
inner join {{ ref('dim_date') }} dd
    on sb.order_date = dd.order_date