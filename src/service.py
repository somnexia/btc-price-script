import requests


from config import REQUEST_TIMEOUT_SECONDS


def fetch_data(url: str) -> dict:
    response = requests.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def extract_price(data: dict, coin_id: str, currency: str):
    price = data.get(coin_id, {}).get(currency)
    if price is None:
        raise ValueError(f"Price not found in API response for {coin_id}/{currency}")
    return price


def send_discord_message(webhook_url: str, content: str) -> None:
    response = requests.post(
        webhook_url,
        json={"content": content},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()