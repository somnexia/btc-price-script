# service.py

# Отвечает за:

# “получить данные с API”
import requests

def fetch_data(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()