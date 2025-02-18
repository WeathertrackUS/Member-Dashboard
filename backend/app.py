from app import create_app
import os

if __name__ == '__main__':
    app = create_app()
    debug_mode = os.getenv('FLASK_ENV') == 'development'  
    app.run(debug=debug_mode) 