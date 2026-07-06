select
    product_id,
    product_category_name,
    product_weight_g
from {{ source('silver', 'SILVER_PRODUCTS') }}
where product_id is not null