import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///wtus_team_system.db'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    ALLOWED_EXTENSIONS = {'psd', 'jpg', 'jpeg', 'png', 'gif'}
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')