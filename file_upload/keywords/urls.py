from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileWithKeywordsViewSet

router = DefaultRouter()

router.register(r"files", FileWithKeywordsViewSet, basename="files")

urlpatterns = [
    path('keywords/', include(router.urls)),
]