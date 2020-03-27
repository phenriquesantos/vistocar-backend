from models import db

class VehicleModel(db.Model):
  id: int = db.Column(db.Integer, primary_key=True)
  client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
  brand: str = db.Column(db.String(30), nullable=False)
  model: str = db.Column(db.String(30), nullable=False)
  board: str = db.Column(db.String(30), nullable=False)
  year: str = db.Column(db.String(30), nullable=False)

  @staticmethod
  def get_by_client(client_id):
    return VehicleModel.query.filter_by(client_id=client_id).first()

  @staticmethod
  def get_by_id(id):
    return VehicleModel.query.filter_by(id=id).first()
