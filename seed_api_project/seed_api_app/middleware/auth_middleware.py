from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from utils.env_helper import ENVHelper
from utils.mongo_helper import MongoHelper
import jwt

class AuthMiddleware(BasePermission):
    def has_permission(self, request, view):
        try:
            auth_header = request.headers.get('Authorization')
            if auth_header == None:
                raise NotAuthenticated()
            envHelper = ENVHelper()
            decode_jwt = jwt.decode(auth_header, envHelper.get("APP_KEY"), algorithms=["HS256"])
            mongoHelper = MongoHelper()
            result = mongoHelper.getCollection("user").find_one(decode_jwt)
            if result != None:
                return True
            raise AuthenticationFailed()
        except Exception as error:
            print(error)
            raise AuthenticationFailed()
        