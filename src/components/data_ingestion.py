import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv') # storing train data in artifacts folder
    test_data_path: str = os.path.join('artifacts', 'test.csv') # storing test data in artifacts folder
    raw_data_path: str = os.path.join('artifacts', 'data.csv') # storing raw data in artifacts folder

class DataIngestion: # data ingestion class where we will perform train test split and store it in artifacts folder
                     # and ingested data will be stored in artifacts folder
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # creating object of DataIngestionConfig class

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')

        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) 
            """
            Create artifacts folder if it doesn't exist and store the train and test data in artifacts folder
            """

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)

            logging.info('Train Test Split initiated')
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)

            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys) # raising custom exception with error message and error details

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))