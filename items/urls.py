from django.urls import path

from .views import ShopView, PotionsAvailable, UsePotion

app_name = 'items'

urlpatterns = [
    path('shop/<int:pk>/', ShopView.as_view(), name='shop'),
    path('potions-available/<int:pk>/', PotionsAvailable.as_view(), name='potions-available'),
    path('use-potion/<str:potion_type>/<int:pk>/', UsePotion.as_view(), name='use-potion'),
]
