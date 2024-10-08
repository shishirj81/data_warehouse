Python script to ingest entire data

import pandas as pd
import ingestion as ing
import sales
import shipments
import products
import vendors
import customers

# ingest folders data into dataframes (assuming wd variable stores location of current working directory)

lst = ['sales','orders_map','shipments']

sales_df, orders_map_df, shipments_df = ing.ingest_folders_data(wd,lst[0]), ing.ingest_folders_data(wd,lst[1]), ing.ingest_folders_data(wd,lst[2])

# ingest json files into dataframes (assuming wd variable stores location of current working directory)

products_df = pd.read_json('wd/products.json')
vendors_df = pd.read_json('wd/vendors.json')
cust_df = pd.read_json('wd/customers.json')

# get dataframes after processing
sales_df_processed = sales.process_sales_data(sales_df)
shipments_df_processed = shipments.process_shipments_data(shipments_df)
products_df_processed = products.process_products_data(products_df)
vendors_df_processed = vendors.process_vendors_data(vendors_df)
vendors_df_processed = vendors.process_vendors_data(vendors_df)
cust_df_processed = customers.process_cust_data(cust_df)


# Merge all the datasets by performing necessary joins (inner joins) on order_id

orders_df = pd.merge(orders_map_df, sales_df, how='inner', on='order_id')
orders_df = pd.merge(orders_df, shipments_df, how='inner', on='shipment_id')
orders_df = pd.merge(orders_df, products_df, how='inner', on='prod_code')
orders_df = pd.merge(orders_df, vendors_df, how='inner', on='vend_code')
orders_df = pd.merge(orders_df, cust_df, how='inner', on='cust_id')

# create feature for final offer price

orders_df['offer_price'] = orders_df['sale_price'] * (1-discount/100.0) + orders_df['shipped_charges']


# Describe the dataframe and display the top 100 rows of final dataframe

print(orders_df.describe())
print(orders_df.head(100))


