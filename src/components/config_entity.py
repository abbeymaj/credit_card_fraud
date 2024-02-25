# Importing packages
import os
import sys
from dataclasses import dataclass

# Creating a class for the Data Ingestion Configuration

@dataclass
class DataIngestionConfig():
    '''
    This class will define the paths for the train data, test data and the raw data.
    '''
    train_data_path:str = os.path.join('artifacts', 'train.zip')
    test_data_path:str = os.path.join('artifacts', 'test.zip')
    #raw_data_path:str = os.path.join('artifacts', 'data.csv')