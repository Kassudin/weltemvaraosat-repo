import sqlite3
from flask import g

DATABASE = 'database.db'

def get_connection():
    con = sqlite3.connect(DATABASE)
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    con = get_connection()
    try:
        con.execute(sql, params)
        con.commit()
    finally:
        con.close()

def query(sql, params=[]):
    con = get_connection()
    try:
        result = con.execute(sql, params).fetchall()
        return result
    finally:
        con.close()