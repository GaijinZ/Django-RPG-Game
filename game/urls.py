from django.urls import path

from .views import HomeView, PlayView, PlayerAttackMonster, MonsterAttackPlayer, CharacterDeath

app_name = 'game'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('play/<int:pk>/', PlayView.as_view(), name='play'),
    path('player-attack-monster/<str:attack_type>/<int:pk>/', PlayerAttackMonster.as_view(), name='player-attack-monster'),
    path('monster-attack-player/<int:pk>/', MonsterAttackPlayer.as_view(), name='monster-attack-player'),
    path('character-death/<int:pk>/', CharacterDeath.as_view(), name='character-death'),
]
