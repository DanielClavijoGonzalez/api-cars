from os import getenv as env
from random import randint

SECRET_KEY = env('secret_key',
                 (str(randint(18425, 94061)) + str(randint(18425, 94061)) +
                  str(randint(18425, 94061)) + str(randint(18425, 94061)) +
                  str(randint(18425, 94061)) + str(randint(18425, 94061)) +
                  str(randint(18425, 94061))
                  ))
