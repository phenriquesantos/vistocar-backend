from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.schedule import ScheduleModel
from datetime import date, datetime


class AvailableTimesResource(Resource):

    def _list_time(self, dt):
        schedules = [
            '08:00',
            '08:30',
            '09:00',
            '09:30',
            '10:00',
            '10:30',
            '11:00',
            '11:30',
            '12:00',
            '12:30',
            '13:00',
            '13:30',
            '14:00',
            '14:30',
            '15:00',
            '15:30',
            '16:00',
            '16:30',
            '17:00',
            '17:30',
            '18:00'
        ]
        dt = dt.split('-')
        times = ScheduleModel.filter_by_date(date(int(dt[2]), int(dt[1]), int(dt[0])))
        for time in times:
            schedules.remove(time.time) if time.time in schedules else False

        return schedules

    # @jwt_required
    def get(self, date):
        try:
            return self._list_time(date)
        except Exception as e:
            return f"{e}", 500
