##### This file contains module to ingest data files from folders ######

import pandas as pd
import os


def ingest_folders_data(wd, arg):
    filepath  = wd + '/' + arg + '/' 
    cnt = 0

    # Start data ingestion into pandas df
    for file in os.listdir(path=filepath):
        if cnt==0:
            df = pd.read_csv(filepath+file+'.csv')
        else:
            temp_df = pd.read_csv(filepath+file+'.csv')
            df = df.append(temp_df)
        cnt+=1

    return df
