# Importing packages
import os
from dataclasses import dataclass

# Creating a class for the Data Ingestion process.

@dataclass
class DataIngestionConfig():
    '''
    This class will define the paths for the train data and test data.
    '''
    train_data_path:str = os.path.join('artifacts', 'train.zip')
    test_data_path:str = os.path.join('artifacts', 'test.zip')


# Creating a class for the Data Transformation process.
@dataclass
class DataTransformationConfig():
    '''
    This class defines the path to the preprocessor object.
    '''
    preprocessor_obj_path:str = os.path.join('artifacts', 'preprocessor.pkl')