from service import fetch_data
from repository import save_price
from config import URL

def main():
    try:
        data = fetch_data(URL)
        price = data.get("bitcoin", {}).get("eur")

        save_price(price)

        print(f"BTC price saved: {price} EUR")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()