from flask import Blueprint, redirect, url_for, request, render_template, flash

from app_state import state

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login", methods=["GET", "POST"])
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
    return redirect(url_for("auth.login"))

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    username = request.form["username"]
    password = request.form["password"]
    if username in state["auth"].keys():
        flash("username exists")
        return redirect(url_for("auth.register"))
    state["auth"][username] = password
    return redirect(url_for("auth.login"))

@auth_blueprint.route("/logout")
def logout():
    state["logged_in"] = False
    state["username"] = None
    return redirect(url_for("index"))