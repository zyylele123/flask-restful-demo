import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app
from ext import db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()