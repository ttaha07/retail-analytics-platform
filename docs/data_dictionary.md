# Data Dictionary

## BRONZE_CUSTOMERS

| Column | Description |
|---|---|
| CUSTOMER_ID | Customer identifier from source system |
| CUSTOMER_UNIQUE_ID | Unique customer identifier |
| CUSTOMER_ZIP_CODE_PREFIX | Customer ZIP code prefix |
| CUSTOMER_CITY | Customer city |
| CUSTOMER_STATE | Customer state |

## BRONZE_ORDERS

| Column | Description |
|---|---|
| ORDER_ID | Unique order identifier |
| CUSTOMER_ID | Customer identifier |
| ORDER_STATUS | Status of the order |
| ORDER_PURCHASE_TIMESTAMP | Timestamp when order was placed |
| ORDER_APPROVED_AT | Timestamp when order was approved |
| ORDER_DELIVERED_CARRIER_DATE | Date delivered to carrier |
| ORDER_DELIVERED_CUSTOMER_DATE | Date delivered to customer |
| ORDER_ESTIMATED_DELIVERY_DATE | Estimated delivery date |

## BRONZE_PRODUCTS

| Column | Description |
|---|---|
| PRODUCT_ID | Unique product identifier |
| PRODUCT_CATEGORY_NAME | Product category |
| PRODUCT_NAME_LENGTH | Product name length |
| PRODUCT_DESCRIPTION_LENGTH | Product description length |
| PRODUCT_PHOTOS_QTY | Number of product photos |
| PRODUCT_WEIGHT_G | Product weight in grams |
| PRODUCT_LENGTH_CM | Product length in centimeters |
| PRODUCT_HEIGHT_CM | Product height in centimeters |
| PRODUCT_WIDTH_CM | Product width in centimeters |

## BRONZE_ORDER_ITEMS

| Column | Description |
|---|---|
| ORDER_ID | Order identifier |
| ORDER_ITEM_ID | Order line item number |
| PRODUCT_ID | Product identifier |
| SELLER_ID | Seller identifier |
| SHIPPING_LIMIT_DATE | Shipping deadline |
| PRICE | Product price |
| FREIGHT_VALUE | Shipping cost |

## FACT_SALES

| Column | Description |
|---|---|
| ORDER_ID | Order identifier |
| PRODUCT_ID | Product identifier |
| CUSTOMER_ID | Customer identifier |
| ORDER_PURCHASE_TIMESTAMP | Timestamp when order was placed |
| PRICE | Product price |
| FREIGHT_VALUE | Shipping cost |

## DIM_CUSTOMER

| Column | Description |
|---|---|
| CUSTOMER_ID | Customer identifier |
| CUSTOMER_UNIQUE_ID | Unique customer identifier |
| CUSTOMER_CITY | Standardized customer city |
| CUSTOMER_STATE | Standardized customer state |

## DIM_PRODUCT

| Column | Description |
|---|---|
| PRODUCT_ID | Product identifier |
| PRODUCT_CATEGORY_NAME | Product category |
| PRODUCT_WEIGHT_G | Product weight in grams |

## DIM_DATE

| Column | Description |
|---|---|
| ORDER_DATE | Order date used for time-based reporting |