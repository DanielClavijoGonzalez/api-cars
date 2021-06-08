import mysql.connector as MC
from os import getenv as env

MYSQL_HOST = env('mysql_host', 'localhost')
MYSQL_USER = env('mysql_user', 'root')
MYSQL_PASSWORD = env('mysql_password', '')
MYSQL_DB = env('mysql_db', 's1tester_api_cars')


class MySQLService:
    def __init__(self):
        self.result = [None, None]

        try:
            self.IDB = MC.connect(host=MYSQL_HOST,
                                  user=MYSQL_USER,
                                  password=MYSQL_PASSWORD,
                                  database=MYSQL_DB)
        except Exception as e:
            print(e)
            self.IDB = None

    def execute(self, query, typeQ):
        if not self.IDB:
            raise Exception("First configure MySQL connection")

        if query is None:
            raise Exception("Set query")

        if typeQ is None:
            raise Exception("Configure query type")

        if typeQ not in [
                'select', 'create', 'update', 'delete', 'select_count'
        ]:
            raise Exception(
                "query type is invalid!, only --> select, create, update, select_count and delete   <--"
            )

        cursor = self.IDB.cursor()

        data_fetch = None

        try:
            cursor.execute(query)

            if typeQ == 'select':
                data_fetch = cursor.fetchall()

            if typeQ != 'select':
                self.IDB.commit()

            cursor.close()

            self.result = [cursor.rowcount, data_fetch]
            return self.result

        except Exception as e:
            print(e)

            cursor.close()
            return self.result
