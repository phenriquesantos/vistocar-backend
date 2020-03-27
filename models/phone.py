from models import db


class PhoneModel(db.Model):
    __tablename__ = 'phone'

    id: int = db.Column(db.Integer, primary_key=True)
    phone: str = db.Column(db.String(25), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    phone_type: int = db.Column(db.Integer, nullable=False)
    last_update = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Date)

    @staticmethod
    def get_by_client(client_id):
        return ScheduleModel.query.filter_by(client_id=client_id).first()

    @staticmethod
    def get_by_id(id):
        return ScheduleModel.query.filter_by(id=id).first()
