from flask import Flask
from flask_wtf import CSRFProtect
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from dotenv import load_dotenv
import os


load_dotenv()

db = SQLAlchemy()
mail = Mail()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Ensure sessions are configured correctly
    app.config['SESSION_TYPE'] = 'filesystem'  # Store sessions in the file system
    app.config['SESSION_PERMANENT'] = False    # Prevent sessions from lasting indefinitely
    app.config['SESSION_USE_SIGNER'] = True    # Sign session cookies for added security
    app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'flask_session')  # Explicit session file storage

    # Ensure the database file exists
    db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../instance/app.db")
    if not os.path.exists(db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        open(db_path, 'w').close()


    # initialize apps
    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from . import main, models
        db.create_all()

    from .main import main
    app.register_blueprint(main)
    
    return app