from django.contrib import admin
from django.urls import path
from . import views


app_name="usuarios"

urlpatterns = [
    path('perfil/<username>', views.get_user_profile, name="userprofile"),
]