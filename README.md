# data_warehouse
**Repository to Ingest and Create Orders Data for Hypermart**

The Data is organized into files and folders from where it is required to be ingested into the flow through python scripts.
The data organization of files and folders and the structure of the data files is explained in data_org.txt file
The python script main.py contains the main program to be executed and all other python scripts are supporting files
Details of Python Srcipts:-
1. ingestion.py - contains module to ingest files from folders into a single pandas dataframe
2. sales.py - module to process sales dataframe
3. shipments.py - module to process shipments dataframe
4. products.py - module to process products dataframe
5. vendors.py - module to process vendors dataframe
6. customers.py - module to process customers dataframe
