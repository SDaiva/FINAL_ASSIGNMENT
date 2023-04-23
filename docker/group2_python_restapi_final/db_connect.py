import mysql.connector
from decouple import config


def crete_connection():
    return mysql.connector.connect(
        host=config('DB_HOST'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        database=config('DB_NAME')
    )
