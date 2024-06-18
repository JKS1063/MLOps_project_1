import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features): # predict function is used to predict the output
        try:
            model_path = 'artifacts\model.pkl' # loading model from artifacts folder
            preprocessor_path = 'artifacts\preprocessor.pkl'  # loading preprocessor from artifacts folder
            model = load_object(file_path = model_path) # loading model
            preprocessor = load_object(file_path = preprocessor_path) # loading model and preprocessor
            data_scaled = preprocessor.transform(features) # transforming data using preprocessor
            preds = model.predict(data_scaled) # predicting on transformed data
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int): 
        # This is responsible for mapping all the inputs that we are giving in the html to beckend with the values
        
        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_eductaion = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_eductaion],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)