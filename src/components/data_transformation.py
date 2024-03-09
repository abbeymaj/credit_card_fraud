# Importing packages
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.components.config_entity import DataTransformationConfig
from src.utils import list_df_column_names
from src.utils import save_object
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

    
    # Creating a function to perform the data transformation
    def initiate_data_transformation(self, train_path:str, test_path:str):
        '''
        This function performs the data transformation on the feature set.
        ===============================================================================
        ----------------
        Parameters:
        ----------------
        train_path : str - The path in which the training data is stored.
        test_path : str - The path in which the test data is stored.
        
        ----------------
        Returns:
        ----------------
        train_arr : numpy array - The array used for training the model.
        test_arr : numpy array - The array used for testing the model.
        preprocessor object path : str - The path in which the preprocessor object 
        is stored.
        ================================================================================
        '''
        try:
            logging.info("Reading the train and test datasets")
            
            # Reading the train and test datasets
            train_df = pd.read_csv(train_path, compression='zip')
            test_df = pd.read_csv(train_path, compression='zip')
            
            logging.info("Instantiating the preprocessing object")
            
            # Instantiating the preprocessor object
            preprocessing_obj = self.create_data_transformation_object()
            
            logging.info("Creating the feature and target sets")
            
            # Defining the target column name
            target_column = "Class"
            
            # Creating the train feature and target sets
            input_feature_train_df = train_df.copy().drop(labels=[target_column], axis=1)
            input_target_train_df = train_df[target_column]
            
            # Creating a test feature and target sets
            input_feature_test_df = test_df.drop(labels=[target_column], axis=1)
            input_target_test_df = test_df[target_column]
            
            logging.info("Preprocessing the train and test datasets")
            
            # Preprocessing the train and test datasets
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            # Combining the train and test feature arrays with the target
            train_arr = np.c_[input_feature_train_arr, np.array(input_target_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(input_target_test_df)]
            
            # Saving the preprocessor object to the artifacts folder
            save_object(
                file_path=DataTransformationConfig.preprocessor_obj_path,
                object=preprocessing_obj
            )
            
            return(
                train_arr,
                test_arr,
                DataTransformationConfig.preprocessor_obj_path
            )
            
         
        except Exception as e:
            raise CustomException(e, sys)
