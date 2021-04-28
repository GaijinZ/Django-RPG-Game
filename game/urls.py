from django.urls import path

from .views import HomeView, PlayView

app_name = 'game'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('play/<int:pk>/', PlayView.as_view(), name='play'),
]
