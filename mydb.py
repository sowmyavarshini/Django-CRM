 
import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection to the MySQL server
    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='1234567*('  # Replace with your MySQL root password
    )

    if dataBase.is_connected():
        cursorObject = dataBase.cursor()

        # Create the database
        cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm")
        print("Database 'dcrm' created successfully or already exists.")
        
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
        print("MySQL connection is closed.")
