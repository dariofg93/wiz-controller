from dataclasses import dataclass
from datetime import datetime


@dataclass
class BulbEntity:
    name: str
    mac_address: str
    ip_address: str
    updated_at: datetime