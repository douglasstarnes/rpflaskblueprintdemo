from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

from app_state import state

@app.route("/")
def index():
    return render_template("index.html", username=state["username"])

@app.route("/login/<user>")
def login(user):
    state["logged_in"] = True
    state["username"] = user
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    state["logged_in"] = False
    state["username"] = None
    return redirect(url_for("index"))

@app.route("/catalog")
def catalog():
    return render_template("catalog.html", items=state["catalog"])

@app.route("/cart")
def cart():
    if not state["logged_in"]:
        return redirect(url_for("index"))
    return render_template("cart.html", items=state["cart"])

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
    return render_template("checkout.html", total=total)

@app.route("/admin")
def admin():
    if not state["logged_in"]:
        return redirect(url_for("index"))
    return render_template("admin.html")
