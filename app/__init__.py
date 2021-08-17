from flask import Flask, app
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)

    # app configurations
    app.config.from_object(config_options[config_name])

    # Initializing database
    db.init_app(app)
    migrate.init_app(app, db)



    return app