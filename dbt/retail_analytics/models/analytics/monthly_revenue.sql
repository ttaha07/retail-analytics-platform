select
    date_trunc('month', order_date) as revenue_month,
    round(sum(total_sale_amount), 2) as total_revenue,
    count(distinct order_id) as total_orders,
    count(distinct customer_unique_id) as total_customers
from {{ ref('fact_sales') }}
group by revenue_month
order by revenue_month