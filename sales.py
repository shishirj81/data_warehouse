##### This file contains module to process sales data ######

import pandas as pd


def process_sales_data(sales_df):

    # Clean values with missing quantity
    sales_df = sales_df[sales_df['order_qty'].isna()!=True]


    # extract useful features from order date field
    sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])
    sales_df['order_day'] = sales_df['order_date'].dt.day
    sales_df['order_dayofweek'] = sales_df['order_date'].dt.dayofweek
    sales_df['order_month'] = sales_df['order_date'].dt.month
    sales_df['order_year'] = sales_df['order_date'].dt.year

    return sales_df
