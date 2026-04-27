# logger.py

# Отвечает за:

# “сохранить цену в лог”
from datetime import datetime

def save(price):
    with open("../logs/btc_log.txt", "a") as f:
        f.write(f"{datetime.now()} BTC: {price} EUR\n")