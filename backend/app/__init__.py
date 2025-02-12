from flask import Flask

app = Flask(__name__)

from .auth import routes as auth_routes
from .routes import assets, schedule, tasks

app.register_blueprint(auth_routes)
app.register_blueprint(assets)
app.register_blueprint(schedule)
app.register_blueprint(tasks)