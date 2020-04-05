import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            "postgres://lycvamwhhudlkq:3d5d6a3ac1d4af6389af3c77ec78647cea4a58b6698b62033a2f6c9bee31c628@ec2-52-73-247-67.compute-1.amazonaws.com:5432/dbfevh9dpc3j56"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
