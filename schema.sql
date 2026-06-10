CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    amount INTEGER NOT NULL
);


INSERT INTO users (username, password) VALUES ('XaPota', 'scrypt:32768:8:1$SAsGarfZzJqWEniE$de5ae17c0683a98ffdb26527a7d666b98225c701860893b9c8b38a4b01a8a3a2915053cc3ac677c084a68d976b27222b256c696659daeb0bd3cc46b07432ac87'); 
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