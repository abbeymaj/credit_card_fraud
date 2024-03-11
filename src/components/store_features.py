# Importing packages
import os
import sys
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.components.config_entity import StoreFeatureConfig


# Creating a class to build the feature store and store the transformed datasets
class FeatureStoreCreation():
    '''
    This class will create the feature store and save the transformed dataset in the
    feature store.
    '''
    # Creating the constructor for the class
    def __init__(self):
        self.feature_store_config = StoreFeatureConfig()
    
    # Creating a function to build the feature store folder
    def create_feature_store(self, train_arr, test_arr):
        '''
        This function creates the feature store folder and store the transformed features
        in the folder. The train feature will be "sharded" into three dataset arrays so
        that they can be uploaded into Github.
        ======================================================================================
        -----------------
        Parameters:
        -----------------
        train_arr : numpy array - This is the combined training dataset array.
        test_arr : numpy array - This is the combined test dataset array.
        
        -----------------
        Returns:
        -----------------
        transformed train array 1 : numpy array - This is the first transformed train array.
        transformed train array 2 : numpy array - This is the second transformed train array.
        transformed train array 3 : numpy array - This is the third transformed train array.
        transformed test array : numpy array - This is the transformed  test array.
        =======================================================================================
        '''
        try:
            # Creating the feature store folder
            dirpath = os.path.dirname(self.feature_store_config.xform_array_train1_path)
            os.makedirs(dirpath, exist_ok=True)
            
            # Splitting the train dataset into three datasets
            arr1, arr2, arr3 = np.array_split(train_arr, 3)
            
            # Saving the three arrays into the feature store folder
            np.save(self.feature_store_config.xform_array_train1_path, arr1)
            np.save(self.feature_store_config.xform_array_train2_path, arr2)
            np.save(self.feature_store_config.xform_array_train3_path, arr3)
            
            # Saving the transformed test set into the feature store folder
            np.save(self.feature_store_config.xform_array_test_path, test_arr)
            
            return(
                self.feature_store_config.xform_array_train1_path,
                self.feature_store_config.xform_array_train2_path,
                self.feature_store_config.xform_array_train3_path,
                self.feature_store_config.xform_array_test_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)
    
    # Loading the split arrays into a combined array and shuffle the data
    def load_array(self, train1_path, train2_path, train3_path):
        '''
        This function loads the three training arrays and combines them into a single 
        training set.
        ==================================================================================
        ----------------
        Parameters:
        ----------------
        train1_path : str - This is the path to the first training array.
        train2_path : str - This is the path to the second training array.
        train3_path : str - This is the path to the third training array.
        
        ----------------
        Returns:
        ----------------
        combined : numpy array - This is the concatenated dataset.
        ==================================================================================
        '''
        try:
            # Loading the three training arrays
            array1 = np.load(train1_path)
            array2 = np.load(train2_path)
            array3 = np.load(train3_path)
            
            # Concatenating the three training arrays
            combined = np.concatenate([array1, array2, array3], axis=0)
            
            return combined
        
        except Exception as e:
            raise CustomException(e, sys)
    
    


