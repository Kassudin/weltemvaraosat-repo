CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    amount INTEGER NOT NULL
);

-- Use `create_admin.py` or a migration/seed step
-- to create or update admin accounts during setup/deployment.
INSERT INTO products (name, amount) VALUES ('polttoainesäiliön korkki', 4);
INSERT INTO products (name, amount) VALUES ('kallistuksen tunnistamisanturi uusi ', 10);
INSERT INTO products (name, amount) VALUES ('kallistuksen tunnistamisanturi vanha', 8);
INSERT INTO products (name, amount) VALUES ('lämpötilan tunnistinanturi', 5 );
INSERT INTO products (name, amount) VALUES ('lämpötilan tunnistinanturi who250', 3);
INSERT INTO products (name, amount) VALUES ('liekkivahti', 31);
INSERT INTO products (name, amount) VALUES ('magneettiventtiili', 6 );
INSERT INTO products (name, amount) VALUES ('polttoainepumppu 0.2 who070', 6);
INSERT INTO products (name, amount) VALUES ('polttoainepumppu 0.3 who090', 5);
INSERT INTO products (name, amount) VALUES ('polttoainepumppu 0.4 who175', 7);
INSERT INTO products (name, amount) VALUES ('puola', 3);
INSERT INTO products (name, amount) VALUES ('polttoainemittari', 6);
INSERT INTO products (name, amount) VALUES ('hiukkassuodatin', 20);
INSERT INTO products (name, amount) VALUES ('palokaasun ulostulon suojapelti', 5);
INSERT INTO products (name, amount) VALUES ('palokaasun suojapellin tiiviste', 9);
INSERT INTO products (name, amount) VALUES ('palotiiviste', 16);
INSERT INTO products (name, amount) VALUES ('0.5 pumppu', 5);
INSERT INTO products (name, amount) VALUES ('Puhallin who-070', 5);
INSERT INTO products (name, amount) VALUES ('magnventtiili', 14);
INSERT INTO products (name, amount) VALUES ('korjaus 0.5 pumppu', 4);

-- Table to record product amount changes (date/time, old -> new)
CREATE TABLE IF NOT EXISTS product_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    product_name TEXT,
    old_amount INTEGER,
    new_amount INTEGER
);