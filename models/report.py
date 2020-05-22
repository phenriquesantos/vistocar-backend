from models import db

class ReportModel(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    status: int = db.Column(db.Integer, nullable=False, default=0)
    vehicle_id: int =  db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    description: str = db.Column(db.String(3000), nullable=False)
    timestamp: str = db.Column(db.Date)

    @staticmethod
    def get_by_client(client_id):
        return ReportModel.query.filter_by(client_id=client_id).all()

    @staticmethod
    def get_by_id(id):
        return ReportModel.query.filter_by(id=id).first()

    @staticmethod
    def list_all():
        return ReportModel.query.order_by(ReportModel.id).all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
