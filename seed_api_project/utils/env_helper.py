import environ
import os
from seed_api_project.settings import BASE_DIR
class ENVHelper:

    def __init__(self):
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
        self.__env = environ.Env()
    
    def get(self, envName, type = "string"):
        try:
            if(type == 'int'):
                return int(self.__env(envName))
            return self.__env(envName)
        except:
            return self.__env(envName)