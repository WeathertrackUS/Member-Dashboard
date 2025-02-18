from flask import Flask, jsonify
from flask_cors import CORS
from backend.config import Config
from backend.app.database import get_db

def create_app():
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
        return jsonify({'message': 'Welcome to WTUS Team System API'})

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def server_error(error):
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
