from dotenv import load_dotenv
load_dotenv()

from config import COIN_ID, CURRENCY, DISCORD_WEBHOOK, URL
from logger import error, info, warning
from repository import save_price
from service import extract_price, fetch_data, send_discord_message


def main():
    try:
        info("Cron job started", event="run_started")

        data = fetch_data(URL)
        price = extract_price(data, COIN_ID, CURRENCY)
        message = f"BTC: {price} {CURRENCY.upper()}"

        info(message, event="price_fetched", price=price, currency=CURRENCY)

    except Exception as e:
        error(str(e), event="run_failed")
        return 1

    exit_code = 0

    try:
        save_price(price, CURRENCY)
        info("Saved to MySQL", event="db_saved", price=price, currency=CURRENCY)
    except Exception as e:
        error(f"MySQL save failed: {e}", event="db_failed")
        exit_code = 1

    if DISCORD_WEBHOOK:
        try:
            send_discord_message(DISCORD_WEBHOOK, message)
            info("Sent to Discord", event="discord_sent")
        except Exception as e:
            error(f"Discord send failed: {e}", event="discord_failed")
            exit_code = 1
    else:
        warning("DISCORD_WEBHOOK is not set; skipping Discord send", event="discord_skipped")
        exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())