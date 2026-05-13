import mysql.connector

from config import DB_CONFIG, missing_database_variables


def get_connection():
    missing = missing_database_variables()
    if missing:
        raise RuntimeError(
            "Missing database environment variables: " + ", ".join(missing)
        )

    return mysql.connector.connect(**DB_CONFIG, connection_timeout=10)