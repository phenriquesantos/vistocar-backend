from datetime import datetime, timedelta
from dateutil.parser import parse
from flask import request
from flask_restful import Resource
from models.user import UserModel
from os import environ
from re import match
from services.email import EmailService
from uuid import uuid4

PASSWORD_PATTERN = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})"
MESSAGE_TEMPLATE = """
Clique no link abaixo para criar uma nova senha:

{0}/#/password-recovery?token={1}&email={2}

Após 10 minutos este link não será mais válido e será necessário iniciar o processo de recuperação de senha novamente.
"""

class UserPasswordRecoveryResource(Resource):
    def get(self):
        email = request.args['email']
        user = UserModel.get_by_email(email)

        if user:
            expiration = datetime.now() + timedelta(seconds=600)

            user.recovery = {'token': str(uuid4()), 'expiration': expiration.isoformat()}
            user.save()

            message = MESSAGE_TEMPLATE.format(environ['ENVIRONMENT_URL'], user.recovery['token'], user.email)

            email_service = EmailService()
            email_service.send(to_address=user.email, message_content=message, subject='D&A in Deals - Recuperação de senha')

            return {'message': 'Recovery message sent'}

        else:
            return {'message': 'User not found'}, 404

    def post(self):
        email = request.json.get('email')
        token = request.json.get('token')
        new_password = request.json.get('password')
        error = None

        user = UserModel.get_by_email(email)

        # Validations
        if not user or not user.recovery:
            error = 'Usuário inválido'

        elif 'token' in user.recovery and user.recovery['token'] != token:
            error = 'Token inválido'

        elif 'expiration' in user.recovery and datetime.now() > parse(user.recovery['expiration']):
            error = 'Token expirado'

        elif not match(PASSWORD_PATTERN, new_password):
            error = 'A senha não atende os critérios mínimos de complexidade'

        if error:
            return {'message': error}, 400

        user.recovery = None
        user.password = UserModel.generate_hash(new_password)
        user.save()

        return None, 204
