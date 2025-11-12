# database/db_manager.py
import sqlite3

class DBManager:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT,
                phone TEXT
            )
        """)
        conn.commit()
        conn.close()

    def register_user(self, username, password, email, phone):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)",
                           (username, password, email, phone))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # username already exists
        finally:
            conn.close()

    def validate_login(self, username, password):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()
        return result is not None
