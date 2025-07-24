import os
from pathlib import Path
import sqlite3
from src.util.constants import DATABASE_PATH

def get_connection():
    # Create the db directory if it does not exist
    db_directory = Path(DATABASE_PATH).parent
    os.makedirs(db_directory, exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn