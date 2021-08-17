from app import create_app, db
from app.models import User, Pitch
from flask_script import Manager, Server

# creating an app instance
app = create_app('development')

manager = Manager(app)


if __name__ == '__main__':
    manager.run()