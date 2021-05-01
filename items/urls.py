from django.urls import path

from .views import ShopView, WeaponDetails, ArmorDetails, SpellDetails, PotionDetails, \
    BuyItems, BuyPotion, SpellsAvailable, PotionsAvailable, UsePotion

app_name = 'items'

urlpatterns = [
    path('shop/<int:pk>/', ShopView.as_view(), name='shop'),
    path('buy-items/<str:item_type>/<int:pk>/', BuyItems.as_view(), name='buy-items'),
    path('buy-potion/<int:pk>/', BuyPotion.as_view(), name='buy-potion'),
    path('spells-available/<int:pk>/', SpellsAvailable.as_view(), name='spells-available'),
    path('potions-available/<int:pk>/', PotionsAvailable.as_view(), name='potions-available'),
    path('weapon-details/<int:pk>/', WeaponDetails.as_view(), name='weapon-details'),
    path('armor-details/<int:pk>/', ArmorDetails.as_view(), name='armor-details'),
    path('spell-details/<int:pk>/', SpellDetails.as_view(), name='spell-details'),
    path('potion-details/<int:pk>/', PotionDetails.as_view(), name='potion-details'),
    path('use-potion/<str:potion_type>/<int:pk>/', UsePotion.as_view(), name='use-potion'),
]
