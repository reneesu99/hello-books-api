from flask import Flask
from .routes import *
def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(hello_world_bp)
    app.register_blueprint(books_bp)
    return app