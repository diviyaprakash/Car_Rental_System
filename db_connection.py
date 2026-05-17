import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="asus",
            database="carrentaldb"
        )
        if connection.is_connected():
            print("Connection successful!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

