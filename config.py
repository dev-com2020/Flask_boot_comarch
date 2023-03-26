import os

class Configuration:
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGE_DIR = os.path.join(STATIC_DIR, 'images')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/_blog.db' % APPLICATION_DIR
    SECRET_KEY = 'secret'
    # SQLALCHEMY_DATABASE_URI = 'postgres:secretpass@localhost:5432/blog_db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

