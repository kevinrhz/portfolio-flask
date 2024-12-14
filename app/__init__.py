from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24) # secret key for CSRF protection
    csrf = CSRFProtect()
    csrf.init_app(app)

    from .main import main
    app.register_blueprint(main)
    
    return app