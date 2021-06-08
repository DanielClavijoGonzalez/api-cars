import time
from flask.views import MethodView
from flask import jsonify, request
from models.apiCarsModel import ApiModelCars


class ApiCars(MethodView):
    def get(self):
        Model = ApiModelCars('get')

        data_fetch = Model.get()

        Result = {'cars': data_fetch}

        return jsonify(Result), 200

    def post(self):
        return "post"

    def put(self):
        return "put"

    def delete(self):
        return "delete"
