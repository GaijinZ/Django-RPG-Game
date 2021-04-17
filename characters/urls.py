from django.urls import path

from .views import CharacterCreationView, CharacterDetailsView, CharacterListView, CharacterInventory

app_name = 'characters'

urlpatterns = [
    path('character-create/', CharacterCreationView.as_view(), name='character-create'),
    path('character-list/<int:pk>/', CharacterListView.as_view(), name='character-list'),
    path('character-details/<int:pk>/', CharacterDetailsView.as_view(), name='character-details'),
    path('character-inventory/<int:pk>/', CharacterInventory.as_view(), name='character-inventory')
]
