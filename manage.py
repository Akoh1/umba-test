from app import create_app, database
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

application = create_app("config")

# app.config.from_object(config('APP_SETTINGS'))
# app.config.from_pyfile('config.py')
# app.config.from_object("config.DevelopmentConfig")


migrate = Migrate(application, database)
manager = Manager(application)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    application.run()
