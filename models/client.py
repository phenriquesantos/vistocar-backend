from models import db


class ClientModel(db.Model):
    __tablename__ = 'client'

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, nullable=True)
    first_name: str = db.Column(db.String(30), nullable=False)
    last_name: str = db.Column(db.String(100), nullable=False)
    cpf: str = db.Column(db.String(11), nullable=False, unique=True)
    rg_number: str = db.Column(db.String(9), nullable=True, unique=True)
    rg_uf: str = db.Column(db.String(2), nullable=True)
    email: str = db.Column(db.String(128), nullable=False, unique=True)
    phone: str = db.Column(db.String(20), nullable=False)
    active: bool = db.Column(db.Boolean, nullable=False, default=True)
    timestamp = db.Column(db.Date)
    # last_login = db.Column(db.Date)

    @staticmethod
    def get_by_email(email):
        return ClientModel.query.filter_by(email=email).first()

    @staticmethod
    def get_by_cpf(cpf):
        return ClientModel.query.filter_by(cpf=cpf).first()

    @staticmethod
    def get_by_rg(rg):
        return ClientModel.query.filter_by(rg_number=rg).first()

    @staticmethod
    def get_by_id(id_client: int):
        return ClientModel.query.filter_by(id=id_client).first()

    @staticmethod
    def get_by_user_id(user_id: int):
        # print(user_id)
        user = ClientModel.query.filter_by(user_id=user_id)
        print(user.all()[0].user_id)
        return user.first()

    @staticmethod
    def get_by_ids(ids_client):
        return ClientModel.query.filter(ClientModel.id.in_(ids_client)).all()

    @staticmethod
    def list_all():
        return ClientModel.query.all()

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
