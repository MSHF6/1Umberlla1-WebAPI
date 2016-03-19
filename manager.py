from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from database import db
from app import create_app
from settings import config

# Create app by factory method
app = create_app(config['default'])
# Get sqlalchemy instance

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
