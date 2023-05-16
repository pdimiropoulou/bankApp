import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://yfpdofqb:gTWrf3VhzCvlOyrFN3nfHlIFJoWDjLKd@kandula.db.elephantsql.com/yfpdofqb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
