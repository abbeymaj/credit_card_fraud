# Importing packages
import sys
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.components.config_entity import StoreFeatureConfig
from src.components.config_entity import ModelTrainerConfig
from src.utils import create_train_set
from src.utils import find_best_model
from src.utils import save_object
from src.utils import calculate_metrics
from sklearn.ensemble import RandomForestClassifier


# Creating a class for model training
class ModelTrainer():
    '''
    This class contains methods to train the ML model.
    '''
    # Creating the constructor
    def __init__(self):
        '''
        The constructor instantiates the modeling training config class.
        '''
        # Instantiating the model trainer config to store the trained model
        self.model_training_config = ModelTrainerConfig()
        # Instantiating the Stored Feature config paths
        self.feature_store_config = StoreFeatureConfig()
    
    
    # Creating a function to initiate the model training
    def create_feature_target_datasets(self):
        '''
        This function creates the feature and target datasets.
        ============================================================================       
        -------------------
        Returns:
        -------------------
        X_train : numpy array - The training feature set.
        y_train : numpy array - The training target set.
        X_test : numpy array - The test feature set.
        y_test : numpy array - The test target set.
        =============================================================================        
        '''
        try:
            logging.info('Creating the feature and target datasets.')
            
            # Combining the training arrays into a single training set
            combined_train_arr = create_train_set(
                self.feature_store_config.xform_array_train1_path,
                self.feature_store_config.xform_array_train2_path,
                self.feature_store_config.xform_array_train3_path
            )
            
            # Loading the test array
            test_array = np.load(self.feature_store_config.xform_array_test_path)
            
            # Dropping the first column from the train and test dataset (time)
            combined_train_arr = combined_train_arr[:, 1:]
            test_array = test_array[:, 1:]
            
            # Splitting the datasets into feature and target sets
            X_train = combined_train_arr[:, :-1]
            y_train = combined_train_arr[:, -1]
            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]
            
            logging.info('Created the feature and target datasets.')
            
            return (
                X_train,
                y_train,
                X_test,
                y_test
            )

        except Exception as e:
            raise CustomException(e, sys)
        
    
    # Creating a function to train the model
    def initiate_model_training(self):
        '''
        This function trains the model and then saves the trained model to the artifacts
        folder.
        ===================================================================================
        ------------------------
        Returns:
        ------------------------
        model_path : str - This is the path to the saved model.
        ====================================================================================
        '''
        try:
            logging.info('Starting the model training process.')
            
            # Getting the feature and target datasets
            X_train, y_train, X_test, y_test = self.create_feature_target_datasets()
            
            # Instantiating the estimator
            rf = RandomForestClassifier(random_state=42)
            
            # Defining the paramters which will be used by grid search to find the best model
            params = {
                'criterion': ['gini', 'entropy', 'log_loss'],
                'max_depth': [None, 3, 6, 8],
                'min_samples_split': [2, 4, 6]
            }
            
            # Generating the best model based on the hyperparameters
            best_model = find_best_model(
                X_train=X_train, 
                y_train=y_train, 
                estimator=rf, 
                params=params,
                cv=5
                )
            
            # Creating the predictions using the test dataset
            y_preds = best_model.predict(X_test)
            
            
            # Evaluating the model using the test dataset
            metric = calculate_metrics(y_true=y_test, y_pred=y_preds)
            
            # Saving the model to the artifacts folder if performance was better than 0.60
            if metric < 0.60:
                raise CustomException("No best model found!")
            else:
                save_object(
                    file_path=self.model_training_config.trained_model_file_path,
                    object=best_model
                    )
            
            logging.info('Model training completed and model saved to artifacts folder.')
            
            return metric
        
        except Exception as e:
            raise CustomException(e, sys)


