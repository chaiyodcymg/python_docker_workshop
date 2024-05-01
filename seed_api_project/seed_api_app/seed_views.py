from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from seed_api_app.middleware.auth_middleware import AuthMiddleware
from rest_framework import status
from utils.mongo_helper import MongoHelper
from rest_framework.exceptions import ParseError

class SeedViews(APIView):

    permission_classes = [AuthMiddleware]

    @swagger_auto_schema(
    operation_description = "Get seed data",
    responses = {
        200: "Success",
        400: "Bad Request",
        401: "Unauthorized",
    }
    )
    def get(self, request):
        try:
            mongoHelper = MongoHelper() 
            result = mongoHelper.getCollection("seed").find()
            return Response(list(result),status=status.HTTP_200_OK)
        except Exception as error: 
            print(error)
            return Response({"message": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            mongoHelper.closeConnection()



    @swagger_auto_schema(
    operation_description = "Add seed data",
    responses = {
        200: "Success",
        400: "Bad Request",
        401: "Unauthorized",
    },
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties = {
            "Seed_RepDate": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_Year": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seeds_YearWeek": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_Varity": openapi.Schema(type=openapi.TYPE_STRING),
            "Seed_RDCSD": openapi.Schema(type=openapi.TYPE_STRING),
            "Seed_Stock2Sale": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_Season": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_Crop_Year": openapi.Schema(type=openapi.TYPE_STRING)
        },
        default = {
            "Seed_RepDate": 25640523,
            "Seed_Year": 2563,
            "Seeds_YearWeek": 26,
            "Seed_Varity": "กข15",
            "Seed_RDCSD": "เลย",
            "Seed_Stock2Sale": 2356,
            "Seed_Season": 1,
            "Seed_Crop_Year": "2563"
        },
        required = ["Seed_RepDate", "Seed_Year", "Seeds_YearWeek" , "Seed_Varity", "Seed_RDCSD", "Seed_Stock2Sale", "Seed_Season", "Seed_Crop_Year"]
    )
    )
    def post(self, request):
        try:
            mongoHelper = MongoHelper() 
            request_body = request.data
            if (
                "Seed_RepDate" in request_body and
                "Seed_Year" in request_body and
                "Seeds_YearWeek" in request_body and
                "Seed_Varity" in request_body and
                "Seed_RDCSD" in request_body and
                "Seed_Stock2Sale" in request_body and
                "Seed_Season" in request_body and
                "Seed_Crop_Year" in request_body
            ):
                result = list(mongoHelper.getCollection("seed").find().sort({"$natural": -1}).limit(1))[0]
                request_body["_id"] = result["_id"] + 1
                mongoHelper.getCollection("seed").insert_one(request_body)
                return Response({"message":"Add data successfully"},status=status.HTTP_200_OK)
            raise ParseError()
        except Exception as error: 
            print(error)
            raise ParseError()
        finally:
            mongoHelper.closeConnection()



    @swagger_auto_schema(
    operation_description = "Edit seed data",
    responses = {
        200: "Success",
        400: "Bad Request",
        401: "Unauthorized",
    },
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties = {
            "_id": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_RepDate": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_Year": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seeds_YearWeek": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_Varity": openapi.Schema(type=openapi.TYPE_STRING),
            "Seed_RDCSD": openapi.Schema(type=openapi.TYPE_STRING),
            "Seed_Stock2Sale": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_Season": openapi.Schema(type=openapi.TYPE_INTEGER),
            "Seed_Crop_Year": openapi.Schema(type=openapi.TYPE_STRING)
        },
        default = {
            "_id": 54,
            "Seed_RepDate": 25650122,
            "Seed_Year": 2562,
            "Seeds_YearWeek": 22,
            "Seed_Varity": "กข12",
            "Seed_RDCSD": "นครพนม",
            "Seed_Stock2Sale": 1334,
            "Seed_Season": 1,
            "Seed_Crop_Year": "2562"
        },
        required = ["_id" ,"Seed_RepDate", "Seed_Year", "Seeds_YearWeek" , "Seed_Varity", "Seed_RDCSD", "Seed_Stock2Sale", "Seed_Season", "Seed_Crop_Year"]
    )
    )
    def put(self, request):
        try:
            mongoHelper = MongoHelper() 
            request_body = request.data
            if (
                "_id" in request_body and
                "Seed_RepDate" in request_body and
                "Seed_Year" in request_body and
                "Seeds_YearWeek" in request_body and
                "Seed_Varity" in request_body and
                "Seed_RDCSD" in request_body and
                "Seed_Stock2Sale" in request_body and
                "Seed_Season" in request_body and
                "Seed_Crop_Year" in request_body
            ):
                mongoHelper.getCollection("seed").update_one({ "_id": request_body["_id"] }, { "$set": request_body })
                return Response({"message": "Edit data successfully"},status=status.HTTP_200_OK)
            raise ParseError()
        except Exception as error: 
            print(error)
            raise ParseError()
        finally:
            mongoHelper.closeConnection()



    @swagger_auto_schema(
    operation_description = "Delete seed data",
    responses = {
        200: "Success",
        400: "Bad Request",
        401: "Unauthorized",
    },
    manual_parameters = [
        openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_STRING , default=54)
    ]   
    )  
    def delete(self, request):
        try:
            mongoHelper = MongoHelper() 
            id = int(request.query_params.get('id'))
            if id != None:
                mongoHelper.getCollection("seed").delete_one({ "_id" : id })
                return Response({"message": "Deleted successfully"} ,status=status.HTTP_200_OK)
            raise ParseError()
        except Exception as error: 
            print(error)
            raise ParseError()
        finally:
            mongoHelper.closeConnection()