import os
import sys
import dill
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):

    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for i in range(len(list(models))): # for loop for all models
            model = list(models.values())[i] # storing model in model variable
            para = params[list(models.keys())[i]] # storing parameters in para variable

            gs = GridSearchCV(model, para, cv = 3)  # passing model and parameters to GridSearchCV
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_) # setting best parameters in model
            model.fit(X_train, y_train) # training model

            y_train_pred = model.predict(X_train) # predicting on training data

            y_test_pred = model.predict(X_test) # predicting on test data

            training_model_score = r2_score(y_train, y_train_pred) # r2 score on training data

            test_model_score = r2_score(y_test, y_test_pred) # r2 score on test data

            report[list(models.keys())[i]] = test_model_score # storing r2 score in report dictionary for each model

        return report
    
    except Exception as e:
        raise CustomException(e, sys)