import mysql.connector
import socket
from config import DB_CONFIG

def get_connection():
    print(socket.gethostname())
    return mysql.connector.connect(**DB_CONFIG)
    