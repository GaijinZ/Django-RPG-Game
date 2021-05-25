from django.urls import path

from game.consumers import PlayerVsPlayerConsumer

websocket_urlpatterns = [
    path('ws/player-vs-player/<str:room_name>', PlayerVsPlayerConsumer.as_asgi()),
]
