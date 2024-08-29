from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.views import BookListAPIView, RetrieveBookViewSet

router = DefaultRouter()
router.register('', RetrieveBookViewSet, basename='book')

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
]

urlpatterns += [
    path('', include(router.urls)),
]
