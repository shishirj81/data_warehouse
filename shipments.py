##### This file contains module to process shipments data ######

import pandas as pd


def process_shipments_data(shipments_df):

    # Impute values with missing shipping charges by 0
    shipments_df['shipped_charges'] = shipments_df['shipped_charges'].fillna(0)


    # extract useful features from shipping date field
    shipments_df['shipped_date'] = pd.to_datetime(shipments_df['shipped_date'])
    shipments_df['shipped_day'] = shipments_df['shipped_date'].dt.day
    shipments_df['shipped_dayofweek'] = shipments_df['shipped_date'].dt.dayofweek
    shipments_df['shipped_month'] = shipments_df['shipped_date'].dt.month
    shipments_df['shipped_year'] = shipments_df['shipped_date'].dt.year

    return shipments_df
