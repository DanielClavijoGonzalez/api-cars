from flask import Flask
from flask_cors import CORS
from routes.routesApi import api_v1
from config.config import SECRET_KEY

app = Flask(__name__, static_url_path='')

app.secret_key = SECRET_KEY

CORS(
    app,
    resources={
        r"/api/v1/cars/": {
            "origins": "*",
            "methods": ["OPTIONS", "GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Authorization", "Content-Type"],
        },
        r"/api/v1/cars/<string:id>/": {
            "origins": ["*"],
            "methods": ["OPTIONS", "GET"],
            "allow_headers": ["Authorization", "Content-Type"],
        },
    },
)

app.add_url_rule(api_v1["api_GPPD"], view_func=api_v1["api_cars_controller"])

app.add_url_rule(api_v1["api_GPPD_byId"],
                 view_func=api_v1["api_cars_byId_controller"])
