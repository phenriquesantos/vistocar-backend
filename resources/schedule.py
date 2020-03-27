from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.schedule import ScheduleModel
from models.vehicle import VehicleModel
from datetime import date, datetime


class ScheduleResource(Resource):

    def _list_scheduling(self):

        schedulings = ScheduleModel.list_all()

        return list(map(lambda scheduling: {
            'id': scheduling.id,
            'status': scheduling.status,
            'client_id': scheduling.client_id,
            'created_at': scheduling.created_at,
            'date': scheduling.date.strftime("%d/%m/%y"),
            'time': scheduling.time
        }, schedulings))

    # @jwt_required
    def get(self):
        try:
            return self._list_scheduling()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                print(item)

                dt = item['date'].split('-')

                model = ScheduleModel()
                model.status = item['status']
                model.created_at = item['created_at']
                model.client_id = item['client_id']
                model.date = date(int(dt[0]), int(dt[1]), int(dt[2]))
                model.time = item['time']
                model.timestamp = date.today()
                model.save()

                vehicle = VehicleModel()
                vehicle.board = item['vehicle_board']
                vehicle.brand = item['vehicle_brand']
                vehicle.model = item['vehicle_model']
                vehicle.year = item['vehicle_year']
                vehicle.save()

                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500


class ScheduleDetailResource(Resource):

    def _get_scheduling(self, id_scheduling):
        scheduling = ScheduleModel.get_by_id(id_scheduling)

        if scheduling is None:
            return {'message': 'Schedule not found'}, 404

        return {
            'id': scheduling.id,
            'status': scheduling.status,
            'client_id': scheduling.client_id,
            'created_at': scheduling.created_at,
            'date': scheduling.date,
            'time': scheduling.time
        }

    # @jwt_required
    def get(self, id):
        try:
            id_scheduling = request.args['id']
            return self._get_scheduling(id_scheduling)

        except Exception as e:
            return f"{e}", 500

    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form
        print(item)
        try:
            if item:
                model = ScheduleModel.get_by_id(int(id))
                if 'status' in item:
                    model.status = item['status']
                if 'created_at' in item:
                    model.created_at = item['created_at']
                if 'client_id' in item:
                    model.client_id = item['client_id']
                if 'date' in item:
                    model.date = item['date']
                if 'time' in item:
                    model.time = item['time']
                model.save()

                return 'edited', 204
            else:
                return 'unedited, invalid payload', 400

        except Exception as e:
            return f"{e}", 500

    def delete(self, id):
        try:
            scheduling = ScheduleModel.get_by_id(id)
            scheduling.delete()
            return 'No Content', 204

        except Exception as e:
            return f"{e}", 500
