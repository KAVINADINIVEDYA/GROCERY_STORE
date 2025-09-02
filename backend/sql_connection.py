import mysql.connector
from mysql.connector import Error

__cnx = None

def get_sql_connection():
    global __cnx
    print("Opening MySQL connection")

    if __cnx is None or __cnx.is_connected() is False:
        try:
            __cnx = mysql.connector.connect(
                host='localhost',  # Specify host for local connection
                user='root',
                password='root',
                database='grocery_store'
            )
            print("Successfully connected to MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            __cnx = None
    return __cnx

def close_sql_connection():
    global __cnx
    if __cnx and __cnx.is_connected():
        __cnx.close()
        print("MySQL connection closed")
        __cnx = None

# Optional: Ensure connection closes on program exit
import atexit
atexit.register(close_sql_connection)