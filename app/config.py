import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # General App Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or '0099719a20118c3584a934e4b2128d1145369eb5cf63e084'
    DEBUG = True

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "../instance/app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CSRF Protection
    WTF_CSRF_ENABLED = True

    # Paths
    UPLOAD_FOLDER = os.path.join(basedir, 'static/uploads')
    STATIC_FOLDER = os.path.join(basedir, 'static')
    TEMPLATES_FOLDER = os.path.join(basedir, 'templates')

    # Security
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_SECURE = False

    # Email Configuration - Flask mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', '1']
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False').lower() in ['true', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'your_email@example.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'your_email_password')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', MAIL_USERNAME)