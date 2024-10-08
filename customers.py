##### This file contains module to process customers data ######

import pandas as pd


def process_cust_data(cust_df):


    # clean-up invalid zip-code values by imputing with Unknown

    def clean(row):
        if row['cust_zip'].isdigit()==False:
            return 'Unknown'
        elif int(row['cust_zip'])>=100000 and int(row['cust_zip'])<=999999:
            return row['cust_zip']
        else:
            return 'Unknown'
            
    cust_df['cust_zip'] = cust_df.apply(clean, axis=1) # apply operation for each row

    return cust_df
