# Importing packages
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.config_entity import DataTransformationConfig
from src.components.config_entity import ModelTrainerConfig
from src.utils import load_object


# Creating the prediction class
class PredictPipeline():
    '''
    This class is used to make predictions using the trained model. The date is transformed
    using the preprocessing object, before using the trained model to make predictions. 
    '''
    # Creating the constructor
    def __init__(self):
        '''
        The constructor instantiates the Data Transformation and Model Trainer
        Config classes.
        '''
        # Instantiating the data transformation object class
        self.data_preprocessing = DataTransformationConfig()
        # Instantiating the model trainer object class
        self.trained_model = ModelTrainerConfig()
    
    # Creating the prediction function
    def predict(self, features):
        '''
        This function makes predictions using the feature inputs from the web page and 
        the trained model. The feature also transforms the input data using the 
        preprocessor object.
        ============================================================================================
        -------------------
        Parameters:
        -------------------
        features : This is the feature data input received from the web page.
        
        -------------------
        Returns:
        -------------------
        preds : This is the prediction based on the input features.
        =============================================================================================
        '''
        try:
            logging.info("Starting the prediction process.")
            
            # Loading the trained model and the preprocessing object
            model = load_object(file_path=self.trained_model)
            preprocessor = load_object(file_path=self.data_preprocessing)
            
            # Transforming the input data using the preprocessor object
            scaled_data = preprocessor.transform(features)
            
            # Predicting using the trained model
            preds = model.predict(scaled_data)
            
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)