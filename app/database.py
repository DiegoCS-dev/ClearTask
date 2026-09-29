import sqlite3

def get_connection():
    return sqlite3.connect("banco.db")