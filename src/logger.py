# Importing packages
import logging
import os
from datetime import datetime


# Creating the format of the log file
LOG_FILE =  f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating the logs directory in the project
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)

# Joining the logs directory path and logs path to create the log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Overriding the basicConfig of logging to include the new log path for the project
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)


