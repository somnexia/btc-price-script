import os

from dotenv import load_dotenv


load_dotenv()


SERVICE_NAME = os.environ.get("SERVICE_NAME", "btc-bot")

COIN_ID = os.environ.get("COIN_ID", "bitcoin")
CURRENCY = os.environ.get("CURRENCY", "eur").lower()
URL = os.environ.get(
    "API_URL",
    f"https://api.coingecko.com/api/v3/simple/price?ids={COIN_ID}&vs_currencies={CURRENCY}",
)

DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

REQUEST_TIMEOUT_SECONDS = int(os.environ.get("REQUEST_TIMEOUT_SECONDS", "30"))
INTERVAL = int(os.environ.get("INTERVAL_SECONDS", "300"))

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT", "3306"))
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

DB_CONFIG = {
    "host": DB_HOST,
    "port": DB_PORT,
    "database": DB_NAME,
    "user": DB_USER,
    "password": DB_PASSWORD,
}


def missing_database_variables() -> list[str]:
    required = {
        "DB_HOST": DB_HOST,
        "DB_NAME": DB_NAME,
        "DB_USER": DB_USER,
        "DB_PASSWORD": DB_PASSWORD,
    }
    return [name for name, value in required.items() if not value]