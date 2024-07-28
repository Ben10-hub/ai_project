import sqlite3
from datetime import datetime

def create_database(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS log (
            license_plate TEXT,
            entry_time TEXT,
            exit_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_entry(db_path, license_plate):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    entry_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO log (license_plate, entry_time) VALUES (?, ?)', (license_plate, entry_time))
    conn.commit()
    conn.close()

def log_exit(db_path, license_plate):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    exit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('UPDATE log SET exit_time = ? WHERE license_plate = ? AND exit_time IS NULL', (exit_time, license_plate))
    conn.commit()
    conn.close()
