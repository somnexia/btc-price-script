from config import DB_NAME, DB_PASSWORD, DB_USER
from database import get_admin_connection, get_connection


def _quote_identifier(identifier: str) -> str:
    return "`" + identifier.replace("`", "``") + "`"


def bootstrap_database_user() -> None:
    conn = get_admin_connection()
    try:
        cursor = conn.cursor()
        try:
            database = _quote_identifier(DB_NAME)
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            cursor.execute(
                "CREATE USER IF NOT EXISTS %s@'%%' IDENTIFIED BY %s",
                (DB_USER, DB_PASSWORD),
            )
            cursor.execute(
                "ALTER USER %s@'%%' IDENTIFIED BY %s",
                (DB_USER, DB_PASSWORD),
            )
            cursor.execute(
                f"GRANT ALL PRIVILEGES ON {database}.* TO %s@'%%'",
                (DB_USER,),
            )
            cursor.execute("FLUSH PRIVILEGES")
            conn.commit()
        finally:
            cursor.close()
    finally:
        conn.close()


def ensure_schema(cursor) -> None:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS btc_prices (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            price DECIMAL(20, 8) NOT NULL,
            currency VARCHAR(10) NOT NULL DEFAULT 'eur',
            fetched_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
    )

    cursor.execute("SHOW COLUMNS FROM btc_prices LIKE 'currency'")
    if cursor.fetchone() is None:
        cursor.execute(
            "ALTER TABLE btc_prices ADD COLUMN currency VARCHAR(10) NOT NULL DEFAULT 'eur'"
        )

    cursor.execute("SHOW COLUMNS FROM btc_prices LIKE 'fetched_at'")
    if cursor.fetchone() is None:
        cursor.execute(
            "ALTER TABLE btc_prices ADD COLUMN fetched_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"
        )


def save_price(price, currency: str) -> None:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        try:
            ensure_schema(cursor)
            cursor.execute(
                """
                INSERT INTO btc_prices (price, currency)
                VALUES (%s, %s)
                """,
                (price, currency),
            )
            conn.commit()
        finally:
            cursor.close()
    finally:
        conn.close()