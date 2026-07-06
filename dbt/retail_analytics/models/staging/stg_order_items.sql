select
    order_id,
    order_item_id,
    product_id,
    price,
    freight_value,
    price + freight_value as total_sale_amount
from {{ source('silver', 'SILVER_ORDER_ITEMS') }}
where order_id is not null
  and order_item_id is not null
  and product_id is not null
  and price is not null
  and price > 0