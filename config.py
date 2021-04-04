import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # database configuration
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URI')
        or 'sqlite:///{}'.format(
            os.path.join(basedir, 'app.db')
            )
    )
    # not track modifications to database structure
    SQLALCHEMY_TRACK_MODIFICATIONS = False
