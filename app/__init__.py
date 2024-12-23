from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()
# print("SECRET_KEY:", os.getenv('SECRET_KEY'))
# print("MAIL_USERNAME:", os.getenv('MAIL_USERNAME'))
# print("MAIL_PASSWORD:", os.getenv('MAIL_PASSWORD'))



mail = Mail()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET KEY', os.urandom(24)) # secret key for CSRF protection

    # Ensure sessions are configured correctly
    app.config['SESSION_TYPE'] = 'filesystem'  # Store sessions in the file system
    app.config['SESSION_PERMANENT'] = False    # Prevent sessions from lasting indefinitely
    app.config['SESSION_USE_SIGNER'] = True    # Sign session cookies for added security
    app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'flask_session')  # Explicit session file storage

    csrf.init_app(app)
    mail.init_app(app)

    # SMTP configuration
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')



    mail.init_app(app) # Initialize the Mail instance with the app here

    from .main import main
    app.register_blueprint(main)
    
    return app