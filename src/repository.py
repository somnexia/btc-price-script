from database import get_connection

def save_price(price):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO btc_prices (price)
        VALUES (%s)
    """

    cursor.execute(query, (price,))
    conn.commit()

    cursor.close()
    conn.close()