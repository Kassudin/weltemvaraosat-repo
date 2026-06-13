import sqlite3
from os import getenv

DATABASE = getenv("DATABASE_PATH", "database.db")

with sqlite3.connect(DATABASE) as con:
    with open("schema.sql", encoding="utf-8") as f:
        con.executescript(f.read())

print("Database initialized.")