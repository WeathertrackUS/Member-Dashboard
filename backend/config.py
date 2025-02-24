import os

class Config:
    DEBUG = False if os.environ.get('DEBUG', '').lower() != 'true' else True
    ALLOWED_EXTENSIONS = {'psd', 'jpg', 'jpeg', 'png', 'gif'}
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
