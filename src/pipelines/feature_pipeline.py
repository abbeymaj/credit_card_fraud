# Importing packages
from src.logger import logging
from src.components.config_entity import DataIngestionConfig
from src.components.data_transformation import DataTransformation
from src.components.store_features import FeatureStoreCreation

# Running the script
if __name__ == '__main__':
    logging.info("Creating the feature store.")
    
    # Getting the train and test data paths
    data_path = DataIngestionConfig()
    train_path = data_path.train_data_path
    test_path = data_path.test_data_path
    
    # Instantiating the data transformation class
    transf_data = DataTransformation()
    train_arr, test_arr, _ = transf_data.initiate_data_transformation(train_path=train_path, test_path=test_path)
    
    # Saving the transformed datasets into the feature store
    store = FeatureStoreCreation()
    store.create_feature_store(train_arr=train_arr, test_arr=test_arr)
    
    logging.info("Feature store created and data transformations completed.")



