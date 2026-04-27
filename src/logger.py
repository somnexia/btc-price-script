# logger.py

# Отвечает за:

# “сохранить цену в лог”
from datetime import datetime
import os

def save(price):
    os.makedirs("logs", exist_ok=True)

    with open("../logs/btc_log.txt", "a") as f:
        f.write(f"{datetime.now()} BTC: {price} EUR\n")