import unittest
import sqlite3
from scripts.log_times import create_database, log_entry, log_exit

class TestLogTimes(unittest.TestCase):
    def setUp(self):
        self.db_path = ':memory:'
        create_database(self.db_path)

    def test_log_entry_exit(self):
        license_plate = 'ABC123'
        log_entry(self.db_path, license_plate)
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT entry_time FROM log WHERE license_plate = ?', (license_plate,))
        entry_time = c.fetchone()
        self.assertIsNotNone(entry_time, "Entry time not logged.")
        log_exit(self.db_path, license_plate)
        c.execute('SELECT exit_time FROM log WHERE license_plate = ?', (license_plate,))
        exit_time = c.fetchone()
        self.assertIsNotNone(exit_time, "Exit time not logged.")
        conn.close()

if __name__ == '__main__':
    unittest.main()
