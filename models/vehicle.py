from models import db


class VehicleModel(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    brand: str = db.Column(db.String(30), nullable=False)
    model: str = db.Column(db.String(30), nullable=False)
    board: str = db.Column(db.String(30), nullable=False, unique=True)
    year: str = db.Column(db.String(30), nullable=False)

    @staticmethod
    def list_all():
        return VehicleModel.query.order_by(VehicleModel.id).all()

    @staticmethod
    def get_by_client(client_id):
        return VehicleModel.query.filter_by(client_id=client_id).all()

    @staticmethod
    def get_by_board(board):
        return VehicleModel.query.filter_by(board=board).first()

    @staticmethod
    def get_by_id(id):
        return VehicleModel.query.filter_by(id=id).first()

    def save(self):
        db.session.merge(self)
        db.session.commit()
