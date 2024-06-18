import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # creating logs folder if it doesn't exist and store the log file in logs folder
os.makedirs(logs_path, exist_ok =  True) # creating logs folder if it doesn't exist and store the log file in logs folder

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # format of the log file to be stored in logs folder
    level = logging.INFO,
)
