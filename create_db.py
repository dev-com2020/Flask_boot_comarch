from app import app
from main import db
import os, sys

sys.path.append(os.getcwd())

with app.app_context():
    db.create_all()

