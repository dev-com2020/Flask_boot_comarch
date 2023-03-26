from flask import Flask, g
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager, current_user

from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)

@app.before_request
def before_request():
    g.user = current_user

