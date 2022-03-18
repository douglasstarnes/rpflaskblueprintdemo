from flask import Blueprint

example_blueprint = Blueprint("example", __name__)

@example_blueprint.route("/")
def example_index():
    return "<h1>Hello Example Blueprint</h1>"
