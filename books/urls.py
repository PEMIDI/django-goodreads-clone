from django.urls import path

from books.views import BookListAPIView, RetrieveBookAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    path('<int:pk>', RetrieveBookAPIView.as_view(), name='book-detail')
]
