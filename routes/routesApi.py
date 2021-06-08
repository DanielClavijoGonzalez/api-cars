from controllers.apiCarsController import ApiCars
from controllers.apiCarsGetByIdController import ApiCarsById

api_v1 = {
    "api_GPPD": "/api/v1/cars/",
    "api_cars_controller": ApiCars.as_view("api_cars_api"),
    # ----------------------------------------------------------------
    "api_GPPD_byId": "/api/v1/cars/<string:id>/",
    "api_cars_byId_controller": ApiCarsById.as_view("api_cars_byId_api"),
}