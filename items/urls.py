from django.urls import path

from .views import ShopView, WeaponDetails, ArmorDetails, SpellDetails

app_name = 'items'

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('weapon-details/<int:pk>/', WeaponDetails.as_view(), name='weapon-details'),
    path('armor-details/<int:pk>/', ArmorDetails.as_view(), name='armor-details'),
    path('spell-details/<int:pk>/', SpellDetails.as_view(), name='spell-details'),
]
