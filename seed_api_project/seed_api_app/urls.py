from django.urls import path
from seed_api_app import views


urlpatterns = [
    path('', views.index),

]
