from django.urls import path
from . import views

urlpatterns = [
    path('chat/default_room/', chat_room, name='chat_room'),

]
