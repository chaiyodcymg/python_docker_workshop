from utils.mongo_helper import MongoHelper,ENVHelper
from Crypto.Hash import SHA256

def initial_user_collection():
    
    mongoHelper = MongoHelper()
    try:
        envHelper = ENVHelper()
        hash_object = SHA256.new()
        hash_object.update(bytes(envHelper.get("ADMIN_PASSWORD"), 'utf-8'))
        hash_object = hash_object.digest()
        data = {
            "_id": 1,
            "username": envHelper.get("ADMIN_USERNAME"),
            "password": hash_object.hex()
        }
        result = mongoHelper.getCollection("user").find()
        if len(list(result)) == 0:
            mongoHelper.getCollection("user").insert_one(data)
            print("=============== initial_user_collection.py ===============\n")
            print("initial_user_collection.py : insert user data successfully.\n")
            print("=============== initial_user_collection.py ===============\n")
        mongoHelper.closeConnection()
        print("=============== initial_user_collection.py ===============\n")
        print("initial_user_collection.py : user data already exists.\n")
        print("=============== initial_user_collection.py ===============\n")
    except Exception as error:
        mongoHelper.closeConnection()
        raise error