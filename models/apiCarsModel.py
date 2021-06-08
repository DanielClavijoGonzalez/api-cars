from services.mysql import MySQLService


class ApiModelCars:
    def __init__(self, action):
        self.action = action

        if self.action not in ['get', 'getById', 'post', 'put', 'delete']:
            raise Exception('Action is not supported, select other')

    def get(self):
        Service = MySQLService()

        data_fetch = Service.execute(query="SELECT * FROM cars",
                                     typeQ="select")

        Result = []

        for field in data_fetch[1]:
            Result.append({
                'id': field[0],
                'name': field[1],
                'brand': field[2],
                'image': field[3],
                'createDate': field[4]
            })

        return Result