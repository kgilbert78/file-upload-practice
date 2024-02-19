from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileUploadViewSet

router = DefaultRouter()

router.register(r"files", FileUploadViewSet, basename="files")

urlpatterns = [
    path('base64api/', include(router.urls)),
]