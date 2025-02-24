import os

class Config:
    DEBUG = os.environ.get('DEBUG', '').lower() == 'true'
    ALLOWED_EXTENSIONS = {'psd', 'jpg', 'jpeg', 'png', 'gif'}
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    ALLOWED_ORIGINS = os.environ.get('ALLOWED_ORIGINS', '').split(',') or ["http://localhost:3000"]
