import os

class Configuration:
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
    SECRET_KEY = 'secret'
    # SQLALCHEMY_DATABASE_URI = 'postgres:secretpass@localhost:5432/blog_db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

