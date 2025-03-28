from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config')

    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=Config.DEBUG)
