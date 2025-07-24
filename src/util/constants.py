import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the .env file
# It is crucial that Load_Dotenv () is called at the beginning, before trying to access the variables.
load_dotenv()

LAMP_1_NAME: str = os.getenv('LAMP_1_NAME')
LAMP_2_NAME: str = os.getenv('LAMP_2_NAME')
LAMP_3_NAME: str = os.getenv('LAMP_3_NAME')
LAMP_4_NAME: str = os.getenv('LAMP_4_NAME')
LAMP_5_NAME: str = os.getenv('LAMP_5_NAME')
LAMP_6_NAME: str = os.getenv('LAMP_6_NAME')

LAMP_1_MAC_ADDRESS: str = os.getenv('LAMP_1_MAC_ADDRESS')
LAMP_2_MAC_ADDRESS: str = os.getenv('LAMP_2_MAC_ADDRESS')
LAMP_3_MAC_ADDRESS: str = os.getenv('LAMP_3_MAC_ADDRESS')
LAMP_4_MAC_ADDRESS: str = os.getenv('LAMP_4_MAC_ADDRESS')
LAMP_5_MAC_ADDRESS: str = os.getenv('LAMP_5_MAC_ADDRESS')
LAMP_6_MAC_ADDRESS: str = os.getenv('LAMP_6_MAC_ADDRESS')


DEFAULT_COLOR_TEMP: int = 3000
DEFAULT_BRIGHTNESS: int = 128

DATA_PATH: str = Path(__file__).resolve().parent.parent.parent / 'data'
# ---Global logger configuration ---
# Obtain the log file from the environment variables
DATABASE_PATH = os.getenv('DATABASE_PATH', DATA_PATH / 'wiz_controller.db')
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', DATA_PATH / 'wiz_controller.log')

LOG_LEVEL_STR = os.getenv('LOG_LEVEL', 'INFO').upper() # Default level if you are not in .env