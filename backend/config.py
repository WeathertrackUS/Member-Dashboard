import os

class Config:
    DEBUG = os.environ.get('DEBUG', '').lower() == 'true'
    ALLOWED_EXTENSIONS = {'psd', 'jpg', 'jpeg', 'png', 'gif'}
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
