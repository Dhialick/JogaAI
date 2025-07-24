from flask import Flask
from app.routes import bp
import os

def criar_app():
    app = Flask(__name__, template_folder=os.path.abspath("templates"), static_folder=os.path.abspath("static"))
    app.register_blueprint(bp)
    return app