import environ
import os

class ENVHelper:

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
        self.env = environ.Env()
    
    def get(self, envName, type = "string"):
        try:
            if(type == 'int'):
                return int(self.env(envName))
            return self.env(envName)
        except:
            return self.env(envName)