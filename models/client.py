from models import db

import random
import string
from datetime import date, datetime

class ClientModel(db.Model):
    __tablename__ = 'client'

    id :int = db.Column(db.Integer, primary_key=True)
    name :str = db.Column(db.String(128), nullable=False)
    email :str = db.Column(db.String(128), nullable=False)
    active :bool = db.Column(db.Boolean, nullable=False, default=True)
    timestamp = db.Column(db.Date)

    @staticmethod
    def get_by_email(email):
        return db.session.query(ClientModel).filter_by(email=email).first()

    @staticmethod
    def get_by_id(id_client :int):
        return db.session.query(ClientModel).filter_by(id=id_client).first()

    @staticmethod
    def get_by_ids(ids_client):
        return db.session.query(ClientModel).filter(ClientModel.id.in_(ids_client)).all()

    @staticmethod
    def list_all():
        return ClientModel.query.order_by(ClientModel.name).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()
