import sqlite3

def create_databases():
    log_db_path = 'parking_log.db'
    membership_db_path = 'memberships.db'
    from .log_times import create_database as create_log_database
    from .subscriptions import create_membership_database

    create_log_database(log_db_path)
    create_membership_database(membership_db_path)

if __name__ == "__main__":
    create_databases()
