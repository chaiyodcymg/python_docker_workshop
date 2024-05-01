from django.urls import path
from seed_api_app import seed_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Seed API",
      default_version='v1',
      description='Authorization Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOjF9.7JcwyUcHRecOj8csHfQrcnDKRY5jiBcccZAqzHjNrcA'
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('seed-data', seed_views.SeedViews.as_view(), name="seed-data"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
