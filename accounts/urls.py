from django.urls import path

from accounts.views import AuthenticateAPIView

urlpatterns = [
    path('', AuthenticateAPIView.as_view(), name='auth'),
]
