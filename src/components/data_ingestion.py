# Importing packages
import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.utils import read_file
from src.components.config_entity import DataIngestionConfig
from sklearn.model_selection import train_test_split


# Creating the data ingestion class
class DataIngestion():
    '''
    This class will ingest the data and split the data into a train and test datasets.
    The train and test datasets will be stored in an "artifacts" folder.
    The raw data will also be retained as as part of the ingestion.
    '''
    # Creating the constructor for the class
    def __init__(self):
        '''
        The constructor instantiates the DataIngestionConfig configuration class. 
        '''
        self.ingestion_config = DataIngestionConfig()
    
    # Creating the function to initiate data ingestion
    def initiate_data_ingestion(self):
        '''
        This function will initiate the data ingestion and also create the artifacts folder.
        ====================================================================================
        ---------------
        Returns:
        ---------------
        train file path : str - This is the path to the train dataset.
        test file path : str - This is the path to the test dataset.
        ====================================================================================
        '''
        logging.info("Starting the data ingestion process.")
        try:
            logging.info("Creating the artifacts directory.")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Reading the dataset into a pandas dataframe
            logging.info("Reading the dataset into a pandas dataframe.")            
            df = read_file('https://gitlab.com/abbeymaj80/datasets/-/raw/master/credit_card.zip')
            
            # Splitting the data into a train set and a test set. Stratifying both datasets
            # using the target feature ("Class").
            logging.info("Splitting the dataset into a train and test set.")
            train_set, test_set = train_test_split(df, test_size=0.33, random_state=42, stratify=df['Class'])
            
            # Saving the train, test and raw datasets to the artifacts folder
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True, compression='zip')
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True, compression='zip')
            
            logging.info("Data ingestion has been completed.")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )  
        
        except Exception as e:
            raise CustomException(e, sys)
        
        
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    