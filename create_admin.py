import os
from werkzeug.security import generate_password_hash
import db

username = os.getenv("ADMIN_USERNAME")
password = os.getenv("ADMIN_PASSWORD")

if not username or not password:
    raise RuntimeError("ADMIN_USERNAME and ADMIN_PASSWORD are required")

password_hash = generate_password_hash(password)

db.execute(
    """
    INSERT INTO users (id, username, password)
    VALUES (1, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        username = excluded.username,
        password = excluded.password
    """,
    [username, password_hash]
)

print("Admin user created/updated.")
