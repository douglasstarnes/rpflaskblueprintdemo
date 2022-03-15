from flask import Blueprint, render_template, redirect, url_for

from app_state import state

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login/<user>")
def login(user):
    state["logged_in"] = True
    state["username"] = user
    return redirect(url_for("index"))

@auth_blueprint.route("/logout")
def logout():
    state["logged_in"] = False
    state["username"] = None
    return redirect(url_for("index"))