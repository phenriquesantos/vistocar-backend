from flask_sqlalchemy import SQLAlchemy
from enum import IntEnum

db :SQLAlchemy = SQLAlchemy()

def create():
    global db
    db.create_all()

def initialize_database(application):
    global db
    db.init_app(application)

class status(IntEnum):
    Active = 0
    Inative = 1
