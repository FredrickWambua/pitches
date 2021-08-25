import os
from app import create_app, db
from app.models import Comment, User, Pitch
from flask_script import Manager, Server
from flask_migrate import Migrate

# creating an app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch = Pitch, Comment = Comment)

if __name__ == '__main__':
    manager.run()