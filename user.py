import db
from flask import session
from werkzeug.security import check_password_hash
import secrets


def login(username, password):
    """Authenticate and set session. Returns True on success."""
    sql = "SELECT id, password FROM users WHERE username = ?"
    result = db.query(sql, [username])
    if not result:
        return False

    user_id = result[0]["id"]
    password_hash = result[0]["password"]
    if check_password_hash(password_hash, password):
        session["user_id"] = user_id
        # ensure a csrf token exists for this session
        if "csrf_token" not in session:
            session["csrf_token"] = secrets.token_hex(16)
        return True
    return False


def logout():
    session.pop("user_id", None)
    session.pop("csrf_token", None)


def is_authenticated():
    return "user_id" in session


def generate_csrf_token():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    return session["csrf_token"]


def validate_csrf(token):
    if not token:
        return False
    return session.get("csrf_token") == token