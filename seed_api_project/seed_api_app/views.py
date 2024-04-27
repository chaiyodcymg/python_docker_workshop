
from django.http import HttpResponse
from utils.mongo_helper import MongoHelper
from utils.env_helper import ENVHelper

# mongoHelper = MongoHelper()

# results = mongoHelper.getConnection().get_collection("startup_log").find()

# for item in results:
#     print("test : "+item["hostname"])

# mongoHelper.closeConnection()

def index(req):

    return HttpResponse("Hello pack")