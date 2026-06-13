CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    amount INTEGER NOT NULL
);

-- Table to record product amount changes (date/time, old -> new)
CREATE TABLE IF NOT EXISTS product_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    product_name TEXT,
    old_amount INTEGER,
    new_amount INTEGER
);
