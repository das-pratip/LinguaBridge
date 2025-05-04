import mysql.connector
from config import DB_CONFIG

def connect_db():
    return mysql.connector.connect(**DB_CONFIG)

def register_user(name, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        print("name:", name)
        print("email:", email)
        print("password:", password)
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        conn.commit()
        return True
    except Exception as ex:
        print(ex)
        return False
    finally:
        conn.close()

def login_user(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None