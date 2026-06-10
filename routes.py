from app import app
from flask import render_template, request, redirect
import user
import products

@app.route('/')
def index():
    list = products.get_all_products()  
    return render_template("index.html", products=list) 

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    user.logout()
    return redirect("/")

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("new_product.html")

    name = request.form.get("name")
    try:
        amount = int(request.form.get("amount"))
    except (TypeError, ValueError):
        return render_template("error.html", message="Virheellinen määrä")

    if products.add_product(name, amount):
        return redirect("/")
    return render_template("error.html", message="Tapahtui virhe")

@app.route("/update_amount", methods=["POST"])
def update_amount():
    product_id = request.form["product_id"]  
    try:
        new_amount = int(request.form["new_amount"])  
    except ValueError:
        return "Virheellinen määrä", 400
    products.update_product_amount(product_id, new_amount)
    return redirect("/")

@app.route("/history")
def history():
    history = products.get_history()
    return render_template("history.html", history=history)

