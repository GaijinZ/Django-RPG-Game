from django.urls import path

from .views import CharacterCreationView, CharacterDetailsView, CharacterListView

app_name = 'characters'

urlpatterns = [
    path('character-create/', CharacterCreationView.as_view(), name='character-create'),
    path('character-list/<int:pk>/', CharacterListView.as_view(), name='character-list'),
    path('character-details/<int:pk>/', CharacterDetailsView.as_view(), name='character-details'),
]
