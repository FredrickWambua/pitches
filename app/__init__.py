from flask import Flask, app
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager

bootstap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)

    # app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # registering the blueprint function
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')



    return app