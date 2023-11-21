import os
import pickle
import sys
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path: str, obj: Any) -> None:
    """
    Save an object to a file using pickle.

    Parameters:
    - file_path (str): The path to the file where the object will be saved.
    - obj (Any): The object to be saved.

    Returns:
    None
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train: pd.DataFrame, y_train: pd.Series, 
                    X_test: pd.DataFrame, y_test: pd.Series,
                    models: Dict[str, Any], param: Dict[str, Any]) -> Dict[str, float]:
    """
    Evaluate machine learning models using GridSearchCV.

    Parameters:
    - X_train (pd.DataFrame): Training data features.
    - y_train (pd.Series): Training data labels.
    - X_test (pd.DataFrame): Test data features.
    - y_test (pd.Series): Test data labels.
    - models (Dict[str, Any]): Dictionary of models to evaluate.
    - param (Dict[str, Any]): Dictionary of model parameters for GridSearchCV.

    Returns:
    Dict[str, float]: A dictionary with model names as keys and R2 scores as values.
    """
    try:
        report = {}

        for model_name, model in models.items():
            params = param[model_name]

            gs = GridSearchCV(model, params, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path: str) -> Any:
    """
    Load an object from a file using pickle.

    Parameters:
    - file_path (str): The path to the file where the object is stored.

    Returns:
    Any: The loaded object.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
