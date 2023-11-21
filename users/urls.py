# users/urls.py
from django.urls import path
from users.views import dashboard,register,edituserprofile


urlpatterns = [

    path("", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("edituserprofile/", edituserprofile, name="edituserprofile"),


]