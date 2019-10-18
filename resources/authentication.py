from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from models.user import UserModel
from os import environ
from datetime import date, datetime


class AuthenticationResource(Resource):

    def post(self):
        data = request.get_json()
        email = data['email'].strip()
        password = data['password']
        user = UserModel.authenticate(email, password)

        if user:
            access = create_jwt({
                'id_user': user.id,
                'email': user.email,
                'name': user.first_name
            })

            return {
                'id_user': user.id,
                'email': user.email,
                'name': user.first_name
            }, 200
        else:
            return {'message': 'Invalid credentials'}, 400
