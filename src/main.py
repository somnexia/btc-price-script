# main.py

# Объединяет:

# получить цену
# вывести
# сохранить
from service import fetch_data
from config import URL, CURRENCY
from logger import save

def main():
    try:
        data = fetch_data(URL)
        price = data.get("bitcoin", {}).get(CURRENCY, "N/A")

        print(f"BTC: {price} EUR")
        save(price)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()