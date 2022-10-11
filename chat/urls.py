from django.urls import path
from .views import *


urlpatterns = [
    path("", chat, name="chat"),
    path("enviarmensaje/", enviarmensaje, name="enviarmensaje"),
    path("leermensajes/", leermensajes, name="leermensajes"),
    

    ]