from src.repository.bulb import table_definition as table_definition_bulb
from src.repository.db import get_connection


def create_tables():
    with get_connection() as conn:
        conn.execute(table_definition_bulb())