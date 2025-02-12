import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///wtus_team_system.db'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    ALLOWED_EXTENSIONS = {'psd', 'jpg', 'jpeg', 'png', 'gif'}
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)