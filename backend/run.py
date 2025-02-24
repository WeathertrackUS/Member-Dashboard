from flask import Flask
from flask_cors import CORS
import logging

from backend.config import Config

def create_app():
    """
    Create a new Flask Application
    """

    # Initialize Flask
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app)

    # Load Configurations
    app.config.from_object(Config)

    # Configure Logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=Config.DEBUG)
