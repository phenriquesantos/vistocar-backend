from models import db


class ScheduleModel(db.Model):
    __tablename__ = 'schedule'

    id: int = db.Column(db.Integer, primary_key=True)
    status: int = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    last_update = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Date)

    @staticmethod
    def get_by_client(client_id):
        return db.session.query(ScheduleModel).filter_by(client_id=client_id).first()

    @staticmethod
    def get_by_status(client_id):
        return db.session.query(ScheduleModel).filter_by(status=status).first()

    @staticmethod
    def get_by_id(id):
        return db.session.query(ScheduleModel).filter_by(id=id).first()
