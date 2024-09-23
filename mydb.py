 
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
load_dotenv()

try:
    # Establish the connection to the MySQL server
    dataBase = mysql.connector.connect(
        host='localhost',
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASS') # Replace with your MySQL root password
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
