##### This file contains module to process products data ######

import pandas as pd


def process_products_data(products_df):

    # calculate category average prices

    prods_dict = {}
    cat_prices = df.groupby(['prod_category']).mean('prod_price')
    for idx in cat_prices.index:
        prods_dict[idx] = cat_prices.loc[idx]['prod_price']


    # impute values with missing product price by avg category price

    products_df['prod_price'] = products_df['prod_price'].fillna(0)

    def impute(row):
        if row['prod_price']!=0:
            return row['prod_price']
        else:
            price = prods_dict[row['prod_category']]
            return price
            
    products_df['prod_price'] = products_df.apply(impute, axis=1) # apply operation for each row

    return products_df
