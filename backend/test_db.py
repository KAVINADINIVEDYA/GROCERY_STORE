from sql_connection import get_sql_connection, close_sql_connection

conn = get_sql_connection()
if conn and conn.is_connected():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    close_sql_connection()
else:
    print("Failed to connect to database")