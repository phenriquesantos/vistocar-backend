from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.schedule import ScheduleModel
from models.vehicle import VehicleModel
from models.client import ClientModel
from datetime import date, datetime


class ScheduleResource(Resource):

    def _list_scheduling(self):

        schedulings = ScheduleModel.list_all()
        res = []
        for scheduling in schedulings:
            client = ClientModel.get_by_id(scheduling.client_id)
            res.append({
                'id': scheduling.id,
                'status': scheduling.status,
                'client_id': scheduling.client_id,
                'created_at': scheduling.created_at,
                'date': scheduling.date.strftime("%d/%m/%y"),
                'time': scheduling.time,
                'client': {
                    'id': client.id,
                    'first_name': client.first_name,
                }
            })

        return res

        # return list(map(lambda scheduling: {
        #     'id': scheduling.id,
        #     'status': scheduling.status,
        #     'client_id': scheduling.client_id,
        #     'created_at': scheduling.created_at,
        #     'date': scheduling.date.strftime("%d/%m/%y"),
        #     'time': scheduling.time,
        # }, schedulings))

    def _list_by_client(self, client_id):
        schedulings = ScheduleModel.get_by_client(client_id)

        res = []
        for scheduling in schedulings:
            client = ClientModel.get_by_id(scheduling.client_id)
            res.append({
                'id': scheduling.id,
                'status': scheduling.status,
                'client_id': scheduling.client_id,
                'created_at': scheduling.created_at,
                'date': scheduling.date.strftime("%d/%m/%y"),
                'time': scheduling.time,
                'client': {
                    'id': client.id,
                    'first_name': client.first_name,
                }
            })

        return res

    def _list_by_date(self, dt):
        schedulings = ScheduleModel.get_by_date(dt)

        res = []
        for scheduling in schedulings:
            client = ClientModel.get_by_id(scheduling.client_id)
            res.append({
                'id': scheduling.id,
                'status': scheduling.status,
                'client_id': scheduling.client_id,
                'created_at': scheduling.created_at,
                'date': scheduling.date.strftime("%d/%m/%y"),
                'time': scheduling.time,
                'client': {
                    'id': client.id,
                    'first_name': client.first_name,
                }
            })

        return res

    # @jwt_required
    def get(self):
        try:
            if request.args.get('client_id'):
                client_id = request.args.get('client_id')
                return self._list_by_client(int(client_id))

            if request.args.get('date'):
                dt = request.args.get('date').split('-')
                dt = date(int(dt[2]), int(dt[1]), int(dt[0]))

                print(dt)

                return self._list_by_date(dt)

            return self._list_scheduling()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:

                if 'vehicle_id' in item and item['vehicle_id'] != "0":
                    vehicle = VehicleModel.get_by_id(int(item['vehicle_id']))
                else:
                    if VehicleModel().get_by_board(item['vehicle_board']):
                        return f'The board "{item["vehicle_board"]}" is already in use.', 400

                    vehicle = VehicleModel()

                vehicle.client_id = int(item['client_id'])
                vehicle.board = item['vehicle_board']
                vehicle.brand = item['vehicle_brand']
                vehicle.model = item['vehicle_model']
                vehicle.year = item['vehicle_year']
                vehicle.save()
                vehicle_saved = vehicle.get_by_board(item['vehicle_board'])

                dt = item['date'].split('-')

                model = ScheduleModel()
                model.status = item['status']
                model.created_at = item['created_at']
                model.client_id = item['client_id']
                model.date = date(int(dt[2]), int(dt[1]), int(dt[0]))
                model.time = item['time']
                model.timestamp = date.today()
                model.vehicle_id = vehicle_saved.id
                model.save()

                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            print(e)
            return f"{e}", 500


class ScheduleDetailResource(Resource):

    def _get_scheduling(self, id_scheduling):
        scheduling = ScheduleModel.get_by_id(id_scheduling)

        if scheduling is None:
            return {'message': 'Schedule not found'}, 404

        client = ClientModel.get_by_id(scheduling.client_id)
        vehicle = VehicleModel.get_by_id(scheduling.vehicle_id)

        dt = str(scheduling.date).split('-')

        return {
            'id': scheduling.id,
            'status': scheduling.status,
            'client_id': scheduling.client_id,
            'created_at': scheduling.created_at,
            'date': dt[2] + '/' + dt[1] + dt[0],
            'time': scheduling.time,
            'client': {
                'id': client.id,
                'first_name': client.first_name
            },
            'vehicle': {
                'id': vehicle.id,
                'brand': vehicle.brand,
                'model': vehicle.model,
                'board': vehicle.board,
                'year': vehicle.year
            }
        }

    # @jwt_required
    def get(self, id):
        try:
            return self._get_scheduling(id)

        except Exception as e:
            return f"{e}", 500

    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form
        print(item)
        try:
            if item:
                if 'vehicle_id' in item and item['vehicle_id'] != "0":
                    vehicle = VehicleModel.get_by_id(int(item['vehicle_id']))
                else:
                    vehicle = VehicleModel()

                if 'vehicle_board' in item:
                    vehicle.board = item['vehicle_board']
                if 'vehicle_brand' in item:
                    vehicle.brand = item['vehicle_brand']
                if 'vehicle_model' in item:
                    vehicle.model = item['vehicle_model']
                if 'vehicle_year' in item:
                    vehicle.year = item['vehicle_year']
                if 'client_id' in item:
                    vehicle.client_id = int(item['client_id'])
                vehicle.save()
                vehicle_saved = vehicle.get_by_board(item['vehicle_board'])
                print(vehicle_saved.id)

                model = ScheduleModel.get_by_id(int(id))
                if 'status' in item:
                    model.status = item['status']
                if 'created_at' in item:
                    model.created_at = item['created_at']
                if 'client_id' in item:
                    model.client_id = item['client_id']
                if 'date' in item:
                    dt = item['date'].split('-')
                    model.date = date(int(dt[2]), int(dt[1]), int(dt[0]))
                if 'time' in item:
                    model.time = item['time']
                if 'vehicle_id' in item:
                    model.vehicle_id = vehicle_saved.id
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
