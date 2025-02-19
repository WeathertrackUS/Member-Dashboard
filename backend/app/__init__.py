from flask import Flask, jsonify
from flask_cors import CORS
from backend.config import Config
from backend.app.database import db_connection
import logging
import os

def create_app():
    """Create a new Flask application and initialize the database if it doesn't exist.

    Returns:
        app: A new Flask application.
        json: A JSON response with an welcome message.
        json: A JSON response with an error message (if necessary).
    """
    app = Flask(__name__)
    # Enable CORS
    CORS(app)
    app.config.from_object(Config)

    # Configure logging for the main application
    Config.configure_logging('Flask-App')
    logger = logging.getLogger(__name__)

    debug_mode = os.getenv('FLASK_ENV')
    if debug_mode == 'development':
        app.debug = True
    elif debug_mode == 'production':
        app.debug = False

    # Initialize database only if it doesn't exist
    with app.app_context(), db_connection() as db:
        cursor = db.cursor()

        # Check if any tables exist
        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='users'
        """)
        table_exists = cursor.fetchone() is not None

        # Create tables only if they don't exist
        if not table_exists:
            schema_path = os.path.join(os.path.dirname(__file__), '..', 'schema.sql')
            with open(schema_path, 'r') as f:
                cursor.executescript(f.read())
            logging.info("Database initialized with schema")

    # Basic index route
    @app.route('/')
    def index():
        """Basic index route.

        Returns:
            json: A JSON response with a welcome message.
        """
        return jsonify({'message': 'Welcome to WTUS Team System API'})

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        """Error handler for 404 errors.

        Args:
            error (string): The error that occurred.

        Returns:
            json: A JSON response with an error message.
        """
        logger.error("404 Error: %s", error)
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def server_error(error):
        """Error handler for 500 errors.

        Args:
            error (string): The error that occurred.

        Returns:
            json: A JSON response with an error message.
        """
        logger.error("500 Error: %s", error)
        return jsonify({'error': 'Internal server error'}), 500

    # Register blueprints
    from backend.app.auth.routes import auth_bp
    from backend.app.routes.assets import assets_bp
    from backend.app.routes.schedule import schedule_bp
    from backend.app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(assets_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(tasks_bp)

    return app
