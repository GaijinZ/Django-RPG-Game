from django.urls import path

from .views import HomeView, PlayView, LobbyView, PlayerVsPlayerView

app_name = 'game'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('play/<int:pk>/', PlayView.as_view(), name='play'),
    path('lobby/', LobbyView.as_view(), name='lobby'),
    path('player-vs-player/', PlayerVsPlayerView.as_view(), name='player-vs-player')
]
