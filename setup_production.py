import os
import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = os.getenv("DATABASE_PATH", "database.db")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if not ADMIN_USERNAME or not ADMIN_PASSWORD:
    raise RuntimeError("ADMIN_USERNAME and ADMIN_PASSWORD are required")

database_dir = os.path.dirname(DATABASE)
if database_dir:
    os.makedirs(database_dir, exist_ok=True)

con = sqlite3.connect(DATABASE)

con.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    amount INTEGER NOT NULL
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS product_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    product_name TEXT,
    old_amount INTEGER,
    new_amount INTEGER
)
""")

password_hash = generate_password_hash(ADMIN_PASSWORD)

con.execute("""
INSERT INTO users (id, username, password)
VALUES (1, ?, ?)
ON CONFLICT(id) DO UPDATE SET
    username = excluded.username,
    password = excluded.password
""", [ADMIN_USERNAME, password_hash])

con.commit()
con.close()

print("Production setup complete.")