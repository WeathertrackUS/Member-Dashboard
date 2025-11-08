from flask import Flask, jsonify
from flask_cors import CORS
import logging

from backend.config import Config


def create_app():
    """Create a new Flask Application"""
    # Initialize Flask
    app = Flask(__name__)

    # Enable and Configure CORS
    CORS(app, resources={
        r"/*": {
            "origins": Config.ALLOWED_ORIGINS,
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Authorization", "Content-Type"]
        }
    })

    # Load Configurations
    app.config.from_object(Config)

    # Configure Logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    # Basic Index Route
    @app.route('/')
    def index():
        """Basic Index Route

        Returns:
            json: A JSON response with a welcome message
        """
        return jsonify({'message': 'Welcome to the WTUS Team System API'})

    @app.errorhandler(404)
    def not_found(error):
        """Error Handler for 404

        Args:
            error (string): Error message

        Returns:
            json: A JSON response with a 404 error message
        """
        logger.error("404 Error: %s", error)
        return jsonify({'error': '404 - Page Not Found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Error Handler for 500

        Args:
            error (string): Error message

        Returns:
            json: A JSON response with a 500 error message
        """
        logger.error("500 Error: %s", error)
        return jsonify({'error': '500 - Internal Server Error'}), 500

    # No Testing needed as this is just a route used to prompt a 500 error for testing purposes
    @app.route('/api/testing/exception/<int:user_id>')
    def test_exception(user_id):
        """Test a 500 Error by raising an Exception

        Args:
            user_id (int): User ID

        Returns:
            json: A JSON response with a 500 error message
        """
        if not Config.DEBUG:
            raise Exception("This route is only available in DEBUG mode")

        if not isinstance(user_id, int):
            raise TypeError("Invalid User ID")
        raise Exception("Database connection failed")

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=Config.DEBUG)
