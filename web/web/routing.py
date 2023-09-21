from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
    ]),
})
