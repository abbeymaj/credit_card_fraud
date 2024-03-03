# Importing packages
import sys
import pandas as pd
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urllib2
from src.exception import CustomException


# Creating a function to read the zipfile on Gitlab
def read_file(file_path:str):
    '''
    This function takes the path to the dataset on Gitlab, which is a zipfile,
    and reads the file into a pandas dataframe.
    ===========================================================================
    -----------------
    Parameters:
    -----------------
    file_path : str - This is the file path to the zipfile on Gitlab
    
    -----------------
    Returns:
    -----------------
    df : dataframe - The function returns a pandas dataframe of the zipped file.
    ============================================================================
    '''
    try:
        res = urllib2.urlopen(file_path).read()
        file = ZipFile(BytesIO(res))
        cc_csv = file.open('credit_card.csv')
        df = pd.read_csv(cc_csv)
        file.close()
        return df 
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function that returns the column names of a dataframe as a list
def list_df_column_names(df_path:str):
    '''
    This function provides a list of the column names from a dataframe.
    ============================================================================
    -----------------
    Parameters:
    -----------------
    df_path : dataframe - The path to the dataframe from which the column names 
    will be listed.
    
    -----------------
    Returns:
    -----------------
    col_list : list - This is a list of the dataframe column names.
    ==============================================================================
    '''
    try:
        df = pd.read_csv(df_path, compression='zip')
        cols = list(df.columns)
        col_list = [x for x in cols if x != 'Class']
        return col_list
    
    except Exception as e:
        raise CustomException(e, sys)
        
    
    
    