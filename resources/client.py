from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.client import ClientModel
from datetime import date, datetime


class ClientResource(Resource):
    def _get_client(self, id_client):
        client = ClientModel.get_by_id(id_client)

        if client is None:
            return {'message': 'Client not found'}, 404

        return {
            'id': client.id,
            'name': client.firt_name,
            'email': client.email,
            'active': client.active
        }

    def _list_client(self):

        clients = ClientModel.list_all()

        return list(map(lambda client: {
            'id': client.id,
            'name': client.first_name,
            'email': client.email,
            'active': client.active
        }, clients))

    @jwt_required
    def get(self):
        if 'id' in request.args:
            id_client = request.args['id']

            return self._get_client(id_client)
        else:
            return self._list_client()

    def post(self):
        item = request.get_json()

        if item:
            model = ClientModel()
            model.first_name = item['first_name']
            model.last_name = item['last_name']
            model.cpf = item['cpf']
            model.rg_number = item['rg_number']
            model.rg_uf = item['rg_uf']
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
                model = ClientModel()
                if 'first_name' in item:
                    model.first_name = item['first_name']
                if 'last_name' in item:
                    model.last_name = item['last_name']
                if 'cpf' in item:
                    model.cpf = item['cpf']
                if 'rg_number' in item:
                    model.rg_number = item['rg_number']
                if 'rg_uf' in item:
                    model.rg_uf = item['rg_uf']
                if 'email' in item:
                    model.email = item['email']
                if 'active' in item:
                    model.active = item['active'] if 'active' in item else True
                model.save()

                return '', 204
            else:
                return '', 400
