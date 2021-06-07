from django.urls import path

from .views import HomeView, PlayView, MonsterAttackPlayer, \
    LobbyView, PlayerVsPlayerView, CharacterDeath

app_name = 'game'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('play/<int:pk>/', PlayView.as_view(), name='play'),
    path('monster-attack-player/<int:pk>/', MonsterAttackPlayer.as_view(), name='monster-attack-player'),
    path('character-death/<int:pk>/', CharacterDeath.as_view(), name='character-death'),
    path('lobby/', LobbyView.as_view(), name='lobby'),
    path('player-vs-player/', PlayerVsPlayerView.as_view(), name='player-vs-player')
]
