from flask import Blueprint, render_template, redirect, url_for

from app_state import state

cart_blueprint = Blueprint("cart", __name__)

@cart_blueprint.route("/view")
def cart():
    if not state["logged_in"]:
        return redirect(url_for("index"))
    return render_template("cart.html", items=state["cart"])

@cart_blueprint.route("/add/<item>")
def cart_add(item):
    if not state["logged_in"]: 
        return redirect(url_for("index"))
    if item in state["catalog"].keys():
        state["cart"].append({"item": item, "cost": state["catalog"][item]})
    return redirect(url_for("cart.cart"))

@cart_blueprint.route("/checkout")
def cart_checkout():
    if not state["logged_in"]:
        return redirect(url_for("index"))
    total = sum([item["cost"] for item in state["cart"]])
    state["cart"].clear()
    return render_template("checkout.html", total=total)
