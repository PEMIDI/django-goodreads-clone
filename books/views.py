from rest_framework.generics import ListAPIView
from django.db.models import Count, Exists, OuterRef
from books.models import Book, Bookmark
from books.paginations import BookStandardPagination
from books.serializers import BookSerializer, AuthenticatedUserBookSerializer


class BookListAPIView(ListAPIView):
    pagination_class = BookStandardPagination

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Book.objects.annotate(
                bookmark_count=Count('bookmarks'),
                is_bookmarked=Exists(Bookmark.objects.filter(book=OuterRef('pk'), user=user))
            )
        else:
            return Book.objects.prefetch_related('bookmarks').annotate(
                bookmark_count=Count('bookmarks')
            )

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return AuthenticatedUserBookSerializer
        else:
            return BookSerializer
