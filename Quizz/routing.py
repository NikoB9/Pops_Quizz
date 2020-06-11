from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/attente_game/(?P<idgame>\w+)/$', consumers.WaitingRoom),
    re_path(r'ws/in_game/(?P<idgame>\w+)/$', consumers.InGame),
    re_path(r'ws/global/$', consumers.Global),
]