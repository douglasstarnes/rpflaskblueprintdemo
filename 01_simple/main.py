from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "yekterces"

from app_state import state

@app.route("/")
def index():
    return render_template("index.html", username=state["username"])

@app.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    username = request.form["username"]
    password = request.form["password"]
    if username in state["auth"].keys() and state["auth"][username] == password:
        state["logged_in"] = True
        state["username"] = username
        return redirect(url_for("index"))
    flash("Wrong username/password")
    return redirect(url_for("login"))

@app.route("/auth/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    username = request.form["username"]
    password = request.form["password"]
    if username in state["auth"].keys():
        flash("username exists")
        return redirect(url_for("register"))
    state["auth"][username] = password
    return redirect(url_for("login"))

@app.route("/auth/logout")
def logout():
    state["logged_in"] = False
    state["username"] = None
    state["cart"].clear()
    return redirect(url_for("index"))

@app.route("/catalog")
def catalog():
    return render_template("catalog.html", items=state["catalog"])

@app.route("/cart/view")
def cart():
    if not state["logged_in"]:
        return redirect(url_for("index"))
    return render_template("cart.html", items=state["cart"], username=state["username"])

@app.route("/cart/add/<item>")
def cart_add(item):
    if not state["logged_in"]: 
        return redirect(url_for("index"))
    if item in state["catalog"].keys():
        state["cart"].append({"item": item, "cost": state["catalog"][item]})
    return redirect(url_for("cart"))

@app.route("/cart/checkout")
def cart_checkout():
    if not state["logged_in"]:
        return redirect(url_for("index"))
    total = sum([item["cost"] for item in state["cart"]])
    state["cart"].clear()
    return render_template("checkout.html", total=total, username=state["username"])

@app.route("/admin")
def admin():
    if not state["logged_in"]:
        return redirect(url_for("index"))
    return render_template("admin.html", username=state["username"])
