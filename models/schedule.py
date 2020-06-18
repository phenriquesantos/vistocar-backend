from models import db


class ScheduleModel(db.Model):
    __tablename__ = 'schedule'

    id: int = db.Column(db.Integer, primary_key=True)
    status: int = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.String(15), nullable=False)
    date = db.Column(db.Date)
    time: str = db.Column(db.String(15), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    timestamp = db.Column(db.Date)
    vehicle_id = db.Column(db.Integer, nullable=False)

    @staticmethod
    def get_by_client(client_id):
        return ScheduleModel.query.filter_by(client_id=client_id).all()

    @staticmethod
    def get_by_status(status):
        return ScheduleModel.query.filter_by(status=status).first()

    @staticmethod
    def filter_by_date(date):
        return ScheduleModel.query.filter_by(date=date).all()

    @staticmethod
    def get_by_id(id: int):
        return ScheduleModel.query.filter_by(id=id).first()

    @staticmethod
    def list_all():
        return ScheduleModel.query.order_by(ScheduleModel.id).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
