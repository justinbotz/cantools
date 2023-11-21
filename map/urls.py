# users/urls.py

from django.urls import path
from map.views import Home

urlpatterns = [
    path("", Home.as_view(), name="map"),
]