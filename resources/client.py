from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.client import ClientModel
from datetime import date, datetime


class ClientResource(Resource):

    def _list_client(self):

        clients = ClientModel.list_all()

        return list(map(lambda client: {
            'id': client.id,
            'name': client.first_name,
            'email': client.email,
            'active': client.active
        }, clients))

    def _get_by_user(self, user_id):
        client = ClientModel.get_by_user_id(user_id)

        if client is None:
            return {'message': 'Client not found'}, 404

        return {
            'id': client.id,
            'first_name': client.first_name,
            'last_name': client.last_name,
            'email': client.email,
            'cpf': client.cpf,
            'phone': client.phone,
            'rg_number': client.rg_number,
            'rg_uf': client.rg_uf,
            'active': client.active
        }

    # @jwt_required
    def get(self):
        try:
            if request.args.get('user_id'):
                user_id = int(request.args.get('user_id'))
                return self._get_by_user(user_id)

            return self._list_client()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:

                if ClientModel().get_by_cpf(item['cpf']):
                    return f'The CPF "{item["email"]}" is already in use.', 400
                if ClientModel().get_by_email(item['email']):
                    return f'The email "{item["email"]}" is already in use.', 400
                if ClientModel().get_by_rg(item['rg_number']):
                    return f'The RG "{item["rg_number"]}" is already in use.', 400

                model = ClientModel()
                model.first_name = item['first_name']
                model.last_name = item['last_name']
                model.cpf = item['cpf']
                model.rg_number = item['rg_number']
                model.rg_uf = item['rg_uf']
                model.email = item['email']
                model.phone = item['phone']
                model.active = item['active'] if 'active' in item else True
                model.user_id = item['user_id'] if 'user_id' in item else None
                model.timestamp = date.today()
                model.save()

                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500




class ClientDetailResource(Resource):

    def _get_client(self, id_client):
        client = ClientModel.get_by_id(id_client)

        if client is None:
            return {'message': 'Client not found'}, 404

        return {
            'id': client.id,
            'first_name': client.first_name,
            'last_name': client.last_name,
            'email': client.email,
            'cpf': client.cpf,
            'phone': client.phone,
            'rg_number': client.rg_number,
            'rg_uf': client.rg_uf,
            'active': client.active
        }

    # @jwt_required
    def get(self, id):
        try:
            return self._get_client(id)

        except Exception as e:
            return f"{e}", 500

    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = ClientModel.get_by_id(id)
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
                if 'phone' in item:
                    model.phone = item['phone']
                if 'active' in item:
                    model.active = item['active'] if 'active' in item else True
                model.save()

                return 'edited', 204
            else:
                return 'unedited, invalid payload', 400

        except Exception as e:
            return f"{e}", 500

    # @jwt_required
    def delete(self, id):
        try:
            client = ClientModel.get_by_id(id)
            vehicles = VehicleModel.get_by_client(id)
            client.delete()
            for vehicle in vehicles:
                vehicle.delete()
            return 'No Content', 204

        except Exception as e:
            return f"{e}", 500
