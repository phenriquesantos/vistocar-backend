from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.user import UserModel
from datetime import date, datetime




class UserResource(Resource):
    def _get_user(self, id_user):
        user = UserModel.get_by_id(id_user)

        if user is None:
            return {'message': 'User not found'}, 404

        return {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'active': user.active
        }

    def _list_user(self):
        users = None

        if 'role' in request.args:
            users = UserModel.get_by_roles(request.args.getlist('role'))
        else:
            users = UserModel.list_all()

        return list(map(lambda user: {
            'id': user.id,
            'name': user.name,
            'company_name': user.company.name,
            'email': user.email,
            'active': user.active
        }, users))

    def get(self):
        claims = get_jwt()

        if 'id' in request.args:
            id_user = request.args['id']

            return self._get_user(id_user)
        else:
            return self._list_user()

    def post(self):
        item = request.get_json()

        if item:
            model = UserModel()
            model.name = item['name']
            model.email = item['email']
            model.active = item['active'] if 'active' in item else True
            model.password = item['password']
            model.timestamp = date.today()
            model.save()

            return '', 201
        else:
            return '', 400

        @jwt_required
        def put(self):
            item = request.get_json()

            if item:
                model = UserModel()
                if 'name' in item:
                    model.name = item['name']
                if 'email' in item:
                    model.email = item['email']
                if 'active' in item:
                    model.active = item['active'] if 'active' in item else True
                if 'password' in item:
                    model.password = item['password']
                model.save()

                return '', 204
            else:
                return '', 400
