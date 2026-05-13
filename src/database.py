import mysql.connector

from config import DB_ADMIN_CONFIG, DB_CONFIG, missing_admin_database_variables, missing_database_variables


def get_connection():
    missing = missing_database_variables()
    if missing:
        raise RuntimeError(
            "Missing database environment variables: " + ", ".join(missing)
        )

    return mysql.connector.connect(**DB_CONFIG, connection_timeout=10)


def get_admin_connection():
    missing = missing_admin_database_variables()
    if missing:
        raise RuntimeError(
            "Missing admin database environment variables: " + ", ".join(missing)
        )

    return mysql.connector.connect(**DB_ADMIN_CONFIG, connection_timeout=10)