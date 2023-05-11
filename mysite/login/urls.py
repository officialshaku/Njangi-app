
from django.urls import path
from .import views


urlpatterns = [
path('login', views.Login_user, name="Login_user"),

]
