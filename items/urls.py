from django.urls import path

from .views import ShopView

app_name = 'items'

urlpatterns = [
    path('shop/<int:pk>/', ShopView.as_view(), name='shop'),
]
