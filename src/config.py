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
    "host": "qtr5dln4tqlvbokvbwlbk3ig",   # имя сервиса в Coolify
    "user": "btc_user",
    "password": "Zaza292472xaxa.",
    "database": "default",
    "port": 3306
}