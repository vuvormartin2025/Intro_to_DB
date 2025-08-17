#!/usr/bin/python3
"""
MySQLServer.py
Creates a database named alx_book_store in MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (update host, user, password as needed)
        connection = mysql.connector.connect(
            host="localhost",      # or your server host
            user="root",           # change if not root
            password="Blaqmartinez@2005" # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to MySQL server or create database.\n{e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()