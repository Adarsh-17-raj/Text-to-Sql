
from sqlite3 import Cursor
import sqlite3
from pathlib import Path
from typing import Any,List,Tuple

DB_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "sample.db"

class DatabaseClient:
    def __init__(self,db_path: Path= DB_PATH):
        self.db_path = db_path
    def get_connection(self) -> sqlite3.Connection:
        """Opens a connection to SQLite in read-only mode for safety"""
        if not self.db_path.exists():
            raise FileNotFoundError(
                f"Database not found at {self.db_path}. Run `uv run python scripts/setup_db.py` first."
            )
        return sqlite3.connect(f"file:{self.db_path}?mode=ro", uri=True)

    def get_schema(self) -> str:
        """Extract DDL schema statement for all the user tables"""
        conn = self.get_connection()
        Cursor = conn.cursor()
        Cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        schemas = [row[0] for row in Cursor.fetchall() if row[0]]
        conn.close()
        return "\n".join(schemas)
    def execute_query(self,query:str) -> Tuple[List[str], List[Tuple[Any, ...]]]:
        """Executes a SELECT query and returns column headers and raw data rows."""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            headers = [desc[0] for desc in cursor.description] if cursor.description else []
            rows = cursor.fetchall()
            return headers, rows
        finally:
            conn.close()