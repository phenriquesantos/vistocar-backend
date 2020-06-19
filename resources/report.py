from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.report import ReportModel
from models.client import ClientModel
from models.vehicle import VehicleModel

from datetime import date, datetime


class ReportResource(Resource):

    def _list_report(self):
        reports = ReportModel.list_all()
        
        res = []
        for report in reports:
            client = ClientModel.get_by_id(report.client_id)
            res.append({
                'id': report.id,
                'status': report.status,
                'client_id': report.client_id,
                'vehicle_id': report.vehicle_id,
                'description': report.description,
                'client': {
                    'id': client.id,
                    'first_name': client.first_name
                }
            })

        return res

    def _list_by_client(self, client_id):
        reports = ReportModel.get_by_client(client_id)

        res = []
        for report in reports:
            client = ClientModel.get_by_id(report.client_id)
            res.append({
                'id': report.id,
                'status': report.status,
                'client_id': report.client_id,
                'vehicle_id': report.vehicle_id,
                'description': report.description,
                'client': {
                    'id': client.id,
                    'first_name': client.first_name
                }
            })

        return res

        # return list(map(lambda report: {
        #     'id': report.id,
        #     'status': report.status,
        #     'client_id': report.client_id,
        #     'vehicle_id': report.vehicle_id,
        #     'description': report.description
        # }, reports))


    # @jwt_required
    def get(self):
        try:
            if request.args.get('client_id'):
                client_id = request.args.get('client_id')
                return self._list_by_client(client_id)
            
            return self._list_report()
        except Exception as e:
            print(e)
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form
        # reports = ReportModel.list_all()

        try:
            if item:
                model = ReportModel()
                model.status = item['status']
                model.vehicle_id = item['vehicle_id']
                model.client_id = item['client_id']
                model.description = item['description']
                model.timestamp = date.today()
                model.save()

                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500




class ReportDetailResource(Resource):

    def _get_report(self, id_report):
        report = ReportModel.get_by_id(id_report)

        if report is None:
            return {'message': 'report not found'}, 404
        
        client = ClientModel.get_by_id(report.client_id)
        vehicle = VehicleModel.get_by_id(report.vehicle_id)

        return {
            'id': report.id,
            'status': report.status,
            'client_id': report.client_id,
            'vehicle_id': report.vehicle_id,
            'client': {
                'id': client.id,
                'first_name': client.first_name
            },
            'vehicle': {
                'model': vehicle.model,
                'board': vehicle.board
            },
            'description': report.description
        }

    # @jwt_required
    def get(self, id):
        try:
            return self._get_report(id)

        except Exception as e:
            return f"{e}", 500

    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = ReportModel()
                model = ReportModel.get_by_id(id)
                if 'status' in item:
                    model.status = item['status']
                if 'vehicle_id' in item:
                    model.vehicle_id = item['vehicle_id']
                if 'client_id' in item:
                    model.client_id = item['client_id']
                if 'description' in item:
                    model.description = item['description']
                model.save()

                return 'edited', 204
            else:
                return 'unedited, invalid payload', 400

        except Exception as e:
            return f"{e}", 500

    def delete(self, id):
        try:
            report = ReportModel.get_by_id(id)
            report.delete()
            return 'No Content', 204

        except Exception as e:
            return f"{e}", 500
