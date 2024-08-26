from django.urls import path

from books.views import BookListAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
]
