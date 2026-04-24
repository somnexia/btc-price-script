import requests
import json

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"

def fetch_data(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    return response.json()

def main():
    try:
        data = fetch_data(URL).get("bitcoin", {}).get("eur", "N/A")
        print(data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()