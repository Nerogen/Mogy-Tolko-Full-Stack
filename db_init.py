import sqlite3


def initialize():
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()

    # Create clients table
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
        account_number INTEGER PRIMARY KEY,
        last_name TEXT,
        first_name TEXT,
        middle_name TEXT,
        date_of_birth DATE,
        inn TEXT,
        responsible_person TEXT,
        status TEXT DEFAULT 'Не в работе'
    )''')

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        username TEXT UNIQUE,
        password TEXT
    )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


def add_user(full_name, username, password):
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)",
                   (full_name, username, password))
    conn.commit()
    conn.close()


def add_client(last_name, first_name, middle_name, date_of_birth, inn, responsible_person):
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clients (last_name, first_name, middle_name, date_of_birth, inn, responsible_person)"
        " VALUES (?, ?, ?, ?, ?, ?)",
        (last_name, first_name, middle_name, date_of_birth, inn, responsible_person))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    initialize()
    add_user('John Doe', 'john', 'password123')
    add_client('Doe', 'Jane', 'Ann', '1990-05-15', '1234567890', 'John Doe')
