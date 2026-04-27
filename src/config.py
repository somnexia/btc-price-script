# config.py

# Хранит настройки:

# URL API
# валюта
# интервал запуска

# Чтобы потом не менять это в 5 местах как варвар.
# URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"
# CURRENCY = "eur"
# INTERVAL = 300  # 5 minutes in seconds

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"

DB_CONFIG = {
    "host": "localhost",
    "user": "labuser",
    "password": "123456",
    "database": "btc"
}