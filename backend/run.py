from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config')

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

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
