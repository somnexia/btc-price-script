from service import fetch_data
from config import URL

def main():
    data = fetch_data(URL)
    price = data.get("bitcoin", {}).get("eur")

    print(f"BTC: {price} EUR")

if __name__ == "__main__":
    main()