"""Config for Flask app."""
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """General config class."""
    DEBUG = False
    CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'dsofpkoasodksap'
    SECRET_KEY = 'zxczxasdsad'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@flask_db:5432/postgres'


class ProductionConfig(Config):
    """Prod config class."""
    DEBUG = False


class DevelopConfig(Config):
    """Develop config class."""
    DEBUG = True
    ASSETS_DEBUG = True
