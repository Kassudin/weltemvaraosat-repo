import db

def add_product(name, amount):
    sql = "INSERT INTO products (name, amount) VALUES (?, ?)"
    db.execute(sql, [name, amount])
    return True

def update_product_amount(product_id, new_amount):
    try:
        pid = int(product_id)
    except (ValueError, TypeError):
        return False

    # fetch existing product to record old amount and name
    rows = db.query("SELECT amount, name FROM products WHERE id = ?", [pid])
    if not rows:
        return False
    # rows are sqlite3.Row so we can use keys
    old_amount = rows[0]["amount"]
    product_name = rows[0]["name"]

    sql = "UPDATE products SET amount = ? WHERE id = ?"
    db.execute(sql, [new_amount, pid])

    # record history; ignore failures if history table missing
    try:
        hist_sql = (
            "INSERT INTO product_history (change_date, product_name, old_amount, new_amount) "
            "VALUES (CURRENT_TIMESTAMP, ?, ?, ?)"
        )
        db.execute(hist_sql, [product_name, old_amount, new_amount])
    except Exception:
        pass

    return True

def get_all_products():
    sql = "SELECT * FROM products ORDER BY name ASC"
    products = db.query(sql)
    return products

def get_history():
    sql = "SELECT change_date, product_name, old_amount, new_amount FROM product_history ORDER BY change_date DESC"
    history = db.query(sql)
    return history