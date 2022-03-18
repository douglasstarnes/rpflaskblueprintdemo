from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "yekterces"

from app_state import state

@app.route("/")
def index():
    return render_template("index.html", username=state["username"])

@app.route("/catalog")
def catalog():
    return render_template("catalog.html", items=state["catalog"])

@app.route("/admin")
def admin():
    if not state["logged_in"]:
        return redirect(url_for("index"))
    return render_template("admin.html", username=state["username"])

from views.example import example_blueprint
from views.auth import auth_blueprint
from views.cart import cart_blueprint

app.register_blueprint(example_blueprint, url_prefix="/example")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(cart_blueprint, url_prefix="/cart")
