from flask.ext.script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
