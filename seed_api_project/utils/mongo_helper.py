import pymongo
from utils.env_helper import ENVHelper

class MongoHelper:
    
    def __init__(self):
        self.__envHelper = ENVHelper()
        self.__connection = pymongo.MongoClient(self.__getDatabaseURL())
        
    def getConnection(self):
        return self.__connection
    
    def getCollection(self, collection_name):
        return self.getConnection().get_database(self.__envHelper.get("DB_NAME")).get_collection(collection_name)
    
    def closeConnection(self):
        self.__connection.close()

    def __getDatabaseURL(self):
        return "mongodb://{username}:{password}@{host}:{port}".format(
            username = self.__envHelper.get("DB_USERNAME") ,
            password = self.__envHelper.get("DB_PASSWORD"),
            host = self.__envHelper.get("DB_HOST"),
            port = self.__envHelper.get("DB_PORT","int"),
        )
        