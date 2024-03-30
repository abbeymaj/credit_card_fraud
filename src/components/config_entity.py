# Importing packages
import os
from dataclasses import dataclass

# Creating a class for the Data Ingestion configuration.

@dataclass
class DataIngestionConfig():
    '''
    This class will define the paths for the train data and test data.
    '''
    train_data_path:str = os.path.join('artifacts', 'train.zip')
    test_data_path:str = os.path.join('artifacts', 'test.zip')


# Creating a class for the Data Transformation Configuration.
@dataclass
class DataTransformationConfig():
    '''
    This class defines the path to the preprocessor object.
    '''
    preprocessor_obj_path:str = os.path.join('artifacts', 'preprocessor.pkl')


# Creating a class for the feature store configuration
@dataclass
class StoreFeatureConfig():
    '''
    This class defines the path for storage location of transformed features
    '''
    xform_array_train1_path:str = os.path.join('feature_store', 'xform_array_train1.npy')
    xform_array_train2_path:str = os.path.join('feature_store', 'xform_array_train2.npy')
    xform_array_train3_path:str = os.path.join('feature_store', 'xform_array_train3.npy')
    xform_array_test_path:str = os.path.join('feature_store', 'xform_array_test.npy')


# Creating a class for the model store configuration
@dataclass
class ModelTrainerConfig():
    '''
    The class defines the path to store and retrieve the trained model object. 
    '''
    trained_model_file_path:str = os.path.join('artifacts', 'model.pkl')