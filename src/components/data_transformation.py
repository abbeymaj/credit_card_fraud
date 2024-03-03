# Importing packages
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.config_entity import DataTransformationConfig
from src.utils import list_df_column_names
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


# Creating a class to perform the data transformation
class DataTransformation():
    '''
    This class contains methods to preprocess the data for the train and test datasets.
    '''
    # Creating the constructor for the class
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    # Defining a function to create the data transformation object
    def create_data_transformation_object(self):
        '''
        This function creates the preprocessing object for data transformation
        '''
        try:
            logging.info('Beginning the creation of the preprocessing object.')
            
            # Creating a list of dataframe columns
            cols = list_df_column_names('artifacts\train.zip')
            
            # Creating the pipeline object
            model_pipeline = Pipeline(
                steps=[
                    ('std_scaler', StandardScaler())
                ]
            )
            
            # Creating the column transformer object
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', model_pipeline, cols)
                ]
            )
            
            logging.info('Completed the creation of the preprocessing object.')
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
