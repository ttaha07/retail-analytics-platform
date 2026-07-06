select
    row_number() over (order by product_id) as product_sk,
    product_id,
    product_category_name,
    product_weight_g,
    current_timestamp() as load_timestamp
from {{ ref('stg_products') }}