# Importing packages
import os
import sys
import dill
import numpy as np
import pandas as pd
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urllib2
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import auc
from sklearn.metrics import precision_recall_curve


# Creating a function to read the zipfile on Gitlab
def read_file(file_path:str):
    '''
    This function takes the path to the dataset on Gitlab, which is a zipfile,
    and reads the file into a pandas dataframe.
    ===========================================================================
    -----------------
    Parameters:
    -----------------
    file_path : str - This is the file path to the zipfile on Gitlab
    
    -----------------
    Returns:
    -----------------
    df : dataframe - The function returns a pandas dataframe of the zipped file.
    ============================================================================
    '''
    try:
        res = urllib2.urlopen(file_path).read()
        file = ZipFile(BytesIO(res))
        cc_csv = file.open('credit_card.csv')
        df = pd.read_csv(cc_csv)
        file.close()
        return df 
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function that returns the column names of a dataframe as a list
def list_df_column_names(df_path:str):
    '''
    This function provides a list of the column names from a dataframe.
    ============================================================================
    -----------------
    Parameters:
    -----------------
    df_path : dataframe - The path to the dataframe from which the column names 
    will be listed.
    
    -----------------
    Returns:
    -----------------
    col_list : list - This is a list of the dataframe column names.
    ==============================================================================
    '''
    try:
        df = pd.read_csv(df_path, compression='zip')
        cols = list(df.columns)
        col_list = [x for x in cols if x != 'Class']
        return col_list
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function that saves an object to the given path
def save_object(file_path:str, object):
    '''
    This function saves as object to the given file path.
    ================================================================================
    --------------------
    Parameters:
    --------------------
    file_path : str - This is path to the folder in which the object will be saved.
    object - This is the object, which will be saved.
    
    --------------------
    Returns:
    --------------------
    Saves the object into folder given in the file path. 
    =================================================================================
    '''
    try:
        # Checking if the folder exists and if not a folder is created
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        # Saving the object using the given path
        with open(file_path, 'wb') as file_obj:
            dill.dump(object, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to load a pickle object
def load_object(file_path:str):
    '''
    This function will load a pickle object.
    ===================================================================================
    ---------------------
    Parameters:
    ---------------------
    file_path : str - This is the path where the object is stored.
    
    ---------------------
    Returns:
    ---------------------
    The function returns the object after it is loaded.
    ==================================================================================== 
    '''
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to load the training arrays and then combine them into a single array
def create_train_set(train_path_1, train_path_2, train_path_3):
    '''
    This function takes the three training arrays as input and combines them into a single
    train array.
    =======================================================================================
    ------------------
    Parameters:
    ------------------
    train_path_1 : str - This is the path to the first training array.
    train_path_2 : str - This is the path to the second training array.
    train_path_3 : str - This is the path to the third training array.
    
    ------------------
    Returns:
    ------------------
    combined_array : numpy array - This is the combined training dataset array.
    ========================================================================================
    '''
    try:
        # Loading the three training array paths
        array_1 = np.load(train_path_1)
        array_2 = np.load(train_path_2)
        array_3 = np.load(train_path_3)
        
        # Combining the three training arrays into a single array.
        combined_array = np.concatenate([array_1, array_2, array_3], axis=0)
        
        return combined_array   
        
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to find the best parameters for the model via Grid Search
def find_best_model(X_train, y_train, estimator, params, cv):
    '''
    This function finds the best parameters for the model, given the parameters for
    that model.
    ================================================================================
    -------------------
    Parameters:
    -------------------
    X_train : numpy array or pandas dataframe - This is the training feature set.
    y_train : numpy array or pandas dataframe - This is the training target set.
    estimator : model object - This is the model that will be used.
    params : dict - This is the parameters, which will be used for the grid search.
    cv : model selection object - This is the cross validation object. 
    
    -------------------
    Returns:
    -------------------
    best_model : model object - This is the model with the best parameters.
    =================================================================================
    '''
    try:
        gs = GridSearchCV(
            estimator=estimator, 
            param_grid=params, 
            cv=cv, 
            scoring='average_precision',
            n_jobs=-1
            )
        gs.fit(X_train, y_train)
        best_model = gs.best_estimator_
        return best_model
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to measure the performance of the model
def calculate_metrics(y_true, y_pred):
    '''
    This function calculates the precision recall under the curve. 
    ===============================================================================================
    --------------------
    Parameters:
    --------------------
    y_true : numpy array or pandas dataframe - This is the labels from the validation or test set.
    y_pred : numpy array or pandas dataframe - This is the predicted values.
    
    --------------------
    Returns:
    --------------------
    prauc : float - This is the precision recall under the curve.
    ===============================================================================================
    '''
    try:
        precisions, recalls, threshold = precision_recall_curve(y_true, y_pred)
        prauc = auc(recalls, precisions)
        return prauc
    
    except Exception as e:
        raise CustomException(e, sys)
    
        
        
    
    
    