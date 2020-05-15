from models import db
from models.user import UserModel
from models.client import ClientModel
from models.schedule import ScheduleModel
from models.report import ReportModel
from models.vehicle import VehicleModel

from datetime import date

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
        if not UserModel.get_by_id(1):
            admin = UserModel()
            admin.first_name = "Admin"
            admin.last_name = ""
            admin.role = "admin "
            admin.email = "admin@admin.com"
            admin.password = "admin123"
            admin.active = True
            admin.timestamp = date.today()
            admin.save()
