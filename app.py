from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

