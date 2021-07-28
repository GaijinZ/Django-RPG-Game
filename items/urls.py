from django.urls import path

from .views import ShopView, WeaponDetails, ArmorDetails, SpellDetails, PotionDetails, \
    SpellsAvailable, PotionsAvailable, UsePotion

app_name = 'items'

urlpatterns = [
    path('shop/<int:pk>/', ShopView.as_view(), name='shop'),
    path('spells-available/<int:pk>/', SpellsAvailable.as_view(), name='spells-available'),
    path('potions-available/<int:pk>/', PotionsAvailable.as_view(), name='potions-available'),
    path('weapon-details/<int:pk>/', WeaponDetails.as_view(), name='weapon-details'),
    path('armor-details/<int:pk>/', ArmorDetails.as_view(), name='armor-details'),
    path('spell-details/<int:pk>/', SpellDetails.as_view(), name='spell-details'),
    path('potion-details/<int:pk>/', PotionDetails.as_view(), name='potion-details'),
    path('use-potion/<str:potion_type>/<int:pk>/', UsePotion.as_view(), name='use-potion'),
]
