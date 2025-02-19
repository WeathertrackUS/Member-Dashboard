from flask import Flask, jsonify
from flask_cors import CORS
from backend.config import Config
from backend.app.database import get_db
import logging 

logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    format='Routing - %(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def create_app():
    """Create a new Flask application and initialize the database.

    Returns:
        app: A new Flask application.
        json: A JSON response with an welcome message.
        json: A JSON response with an error message (if necessary).
    """
    app = Flask(__name__)
    # Enable CORS
    CORS(app)
    app.config.from_object(Config)

    # Initialize database
    with app.app_context():
        db = get_db()
        with app.open_resource('../schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        db.close()

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
        logging.error("Error 404: %s", error)
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def server_error(error):
        """Error handler for 500 errors.

        Args:
            error (string): The error that occurred.

        Returns:
            json: A JSON response with an error message.
        """
        logging.error("Error 500: %s", error)
        return jsonify({'error': 'Internal server error'}), 500

    # Register blueprints
    from app.auth.routes import auth_bp
    from app.routes.assets import assets_bp
    from app.routes.schedule import schedule_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(assets_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(tasks_bp)

    return app
