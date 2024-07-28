import sqlite3
from datetime import datetime, timedelta

def create_membership_database(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS memberships (
            license_plate TEXT PRIMARY KEY,
            membership_type TEXT,
            expiry_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_membership(db_path, license_plate, membership_type, duration_days):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    expiry_date = (datetime.now() + timedelta(days=duration_days)).strftime('%Y-%m-%d')
    c.execute('INSERT OR REPLACE INTO memberships (license_plate, membership_type, expiry_date) VALUES (?, ?, ?)', (license_plate, membership_type, expiry_date))
    conn.commit()
    conn.close()

def check_membership(db_path, license_plate):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT membership_type, expiry_date FROM memberships WHERE license_plate = ?', (license_plate,))
    result = c.fetchone()
    conn.close()
    if result:
        membership_type, expiry_date = result
        if datetime.strptime(expiry_date, '%Y-%m-%d') > datetime.now():
            return membership_type, expiry_date
    return None, None
