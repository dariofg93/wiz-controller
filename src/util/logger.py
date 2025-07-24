import logging
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the .env file
# It is crucial that Load_Dotenv () is called at the beginning, before trying to access the variables.
load_dotenv()

# ---Global logger configuration ---
# Obtain the log file from the environment variables
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH')
LOG_LEVEL_STR = os.getenv('LOG_LEVEL', 'INFO').upper() # Default level if you are not in .env

# Convert the Log level string to its numeric logging value
LOG_LEVEL = getattr(logging, LOG_LEVEL_STR, logging.INFO)

# Create the log directory if it does not exist
log_directory = Path(LOG_FILE_PATH).parent
os.makedirs(log_directory, exist_ok=True)

# Obtain the LOGGER instance (we use a fixed name for the application logger)
_app_logger = logging.getLogger('WizControllerLogger')
_app_logger.setLevel(LOG_LEVEL)

# Configure the formatter
_formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

# Configure the Filehandler (to write in the file)
# Check if the handler already exists to avoid duplicates in module recharges
if not any(isinstance(handler, logging.FileHandler) and handler.baseFilename == os.path.abspath(LOG_FILE_PATH) for handler in _app_logger.handlers):
    _file_handler = logging.FileHandler(LOG_FILE_PATH, encoding='utf-8')
    _file_handler.setFormatter(_formatter)
    _app_logger.addHandler(_file_handler)

# Optional: configure a streamhandler to also print on the console
# If you do not want output on the console, you can comment or eliminate these lines
if not any(isinstance(handler, logging.StreamHandler) for handler in _app_logger.handlers):
    _console_handler = logging.StreamHandler()
    _console_handler.setFormatter(_formatter)
    _app_logger.addHandler(_console_handler)


# ---Static methods for external use ---

def debug(message: str, *args, **kwargs):
    """Registra un mensaje con nivel DEBUG."""
    _app_logger.debug(message, *args, **kwargs)

def info(message: str, *args, **kwargs):
    """Registra un mensaje con nivel INFO."""
    _app_logger.info(message, *args, **kwargs)

def warning(message: str, *args, **kwargs):
    """Registra un mensaje con nivel WARNING."""
    _app_logger.warning(message, *args, **kwargs)

def error(message: str, *args, **kwargs):
    """Registra un mensaje con nivel ERROR."""
    _app_logger.error(message, *args, **kwargs)

def critical(message: str, *args, **kwargs):
    """Registra un mensaje con nivel CRITICAL."""
    _app_logger.critical(message, *args, **kwargs)