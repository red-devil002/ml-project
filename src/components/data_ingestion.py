import os
import sys
from src.exception import CustomException
from src.logger import logging

# Cor Libs
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # use for creating data classes - custom data structures/Function vars


# Data Ingestion Configuration - store the incoming data likes saving data path, train paths, and etc.
@dataclass # decorator to automatically generate special methods like __init__()
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        # Read the data from source
        try:
            df = pd.read_csv('notebooks/data/stud.csv')
            logging.info("Read the datasets")

            

        except:
            pass