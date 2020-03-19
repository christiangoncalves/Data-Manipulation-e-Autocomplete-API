from flask import Flask
from flask_migrate import Migrate
from .model import configure
from .serealizer import configure as config_serealizer
from .timeline_bp import timeline_bp
import os

def create_app():
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    URI = "sqlite:///" + os.path.join(PROJECT_ROOT, 'timeline.db')

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure(app)
    config_serealizer(app)

    Migrate(app, app.db)

    app.register_blueprint(timeline_bp)
    
    return app