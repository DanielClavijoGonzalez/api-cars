import time
from flask.views import MethodView
from flask import jsonify, request


class ApiCarsById(MethodView):
    def get(self, id):
        return "get by id"