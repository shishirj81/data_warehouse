##### This file contains module to process vendors data ######

import pandas as pd


def process_vendors_data(vendors_df):


    # impute values with missing product price by avg category price

    def clean(row):
        if row['vend_contact'].isdigit()==False:
            return 'Unknown'
        else:
            return row['vend_contact']
            
    vendors_df['vend_contact'] = vendors_df.apply(clean, axis=1) # apply operation for each row

    return vendors_df
