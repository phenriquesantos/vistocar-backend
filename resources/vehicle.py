from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.vehicle import VehicleModel


class VehicleResource(Resource):

    def _list_vehicle(self):
        vehicles = VehicleModel.list_all()

        return list(map(lambda vehicle: {
            'id': vehicle.id,
            'client_id': vehicle.client_id,
            'brand': vehicle.brand,
            'model': vehicle.model,
            'board': vehicle.board,
            'year': vehicle.year
        }, vehicles))

    def _list_by_client(self, client_id):
        vehicles = VehicleModel.get_by_client(client_id)

        return list(map(lambda vehicle: {
            'id': vehicle.id,
            'client_id': vehicle.client_id,
            'brand': vehicle.brand,
            'model': vehicle.model,
            'board': vehicle.board,
            'year': vehicle.year
        }, vehicles))

    # @jwt_required
    def get(self):
        try:
            if request.args.get('client_id'):
                client_id = request.args.get('client_id')
                return self._list_by_client(int(client_id))

            return self._list_vehicle()
        except Exception as e:
            return f"{e}", 500
