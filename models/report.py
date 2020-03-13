from models import db

class ReportModel(db.model){
  id: int = db.Column(db.Integer, primary_key=True)
  status: bool = db.Column(db.Boolean, nullable=False)
  vehicle_id: int =  db.Column(db.Integer, nullable=False)
  client_id: int = db.Column(db.Integer, nullable=False)
  user_id: int = db.Column(db.Integer, nullable=False)
  timestamp: str = db.Column(db.Date)

  @staticmethod
  def get_by_client(client_id):
    return ScheduleModel.query.filter_by(client_id=client_id).first()

  @staticmethod
  def get_by_id(id):
    return ScheduleModel.query.filter_by(id=id).first()

  def get_by_user(user_id):
    return ScheduleModel.query.filter_by(user_id=user_id)

}