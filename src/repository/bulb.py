from typing import List
from src.repository.db import get_connection
from src.model.bulb import BulbEntity
from datetime import datetime


def table_definition() -> str:
    return"""
    CREATE TABLE IF NOT EXISTS bulb (
        name TEXT PRIMARY KEY,
        mac_address TEXT NOT NULL,
        ip_address TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """

class BulbRepository:

    def get(self, name: str) -> BulbEntity | None:
        with get_connection() as conn:
            row = conn.execute("SELECT * FROM bulb WHERE name = ?", (name,)).fetchone()
            if row:
                return BulbEntity(
                    name=row["name"],
                    mac_address=row["mac_address"],
                    ip_address=row["ip_address"],
                    updated_at=datetime.fromisoformat(row["updated_at"])
                )
            return None

    def retrieve(self) -> List[BulbEntity]:
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM bulb").fetchall()
            return [
                BulbEntity(
                    name=row["name"],
                    mac_address=row["mac_address"],
                    ip_address=row["ip_address"],
                    updated_at=datetime.fromisoformat(row["updated_at"])
                )
                for row in rows
            ]

    def insert_or_update(self, bulb: BulbEntity):
        now = datetime.now().isoformat()

        with get_connection() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO bulb (name, mac_address, ip_address, updated_at)
                VALUES (?, ?, ?, ?)
            """, (bulb.name, bulb.mac_address, bulb.ip_address, now))

    def delete(self, name: str) -> bool:
        with get_connection() as conn:
            cursor = conn.execute("DELETE FROM bulb WHERE name = ?", (name,))
            return cursor.rowcount > 0
