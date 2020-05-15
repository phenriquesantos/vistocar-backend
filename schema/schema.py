from models import db
from models.user import UserModel
from models.client import ClientModel
from models.schedule import ScheduleModel
from models.report import ReportModel
from models.vehicle import VehicleModel

from os import environ
# importar model aqui

from sqlalchemy import create_engine


class Schema:
    @staticmethod
    def migration():
        # aqui alteramos o banco
        engine = create_engine(environ.get('SQLALCHEMY_DATABASE_URI'))
        # <ClassModelName>.__table__.drop(engine)
        db.create_all()
