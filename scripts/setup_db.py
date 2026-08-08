import sqlite3
import sys
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "sample.db"
CHINOOK_URL = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"

def download_database():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if DB_PATH.exists():
        print(f"[INFO] Database already exists at: {DB_PATH}")
        return 
    print("[INFO] Downloading Chinook SQLite database...")
    try:
        urllib.request.urlretrieve(CHINOOK_URL, DB_PATH)
        print(f"[SUCCESS] Database saved to {DB_PATH}")
    except Exception as e:
        print(f"[ERROR] Failed download: {e}", file=sys.stderr)
        sys.exit(1)

def verify_database():
    if not DB_PATH.exists():
        print("[ERROR] Database file missing.", file=sys.stderr)
        sys.exit(1)
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall() if not row[0].startswith("sqlite_")]

        print("\n--- Database Verification ---")
        print(f"Path: {DB_PATH}")
        print(f"Total Tables: {len(tables)}")
        print(f"Tables: {', '.join(tables)}")

        cursor.execute("SELECT COUNT(*) FROM Customer;")
        print(f"Customer Count: {cursor.fetchone()[0]}")
        conn.close()
        print("--- Verification Passed ---\n")
    except sqlite3.Error as e:
        print(f"[ERROR] SQLite error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    download_database()
    verify_database()
