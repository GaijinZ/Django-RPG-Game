from django.urls import path

from .views import RegisterView, ActivateAccount, LoginView

app_name = 'accounts'

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('sign-in/', LoginView.as_view(), name='sign-in')
]
