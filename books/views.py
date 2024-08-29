from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Count, Exists, OuterRef, Avg, Case, When, IntegerField

from books.models import Book, Bookmark
from books.paginations import BookStandardPagination
from books.serializers import BookSerializer, AuthenticatedUserBookSerializer, BookDetailSerializer


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


class RetrieveBookAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def get_queryset(self):
        return super().get_queryset().prefetch_related('reviews').annotate(
            score_1_count=Count(Case(When(reviews__score=1, then=1), output_field=IntegerField())),
            score_2_count=Count(Case(When(reviews__score=2, then=1), output_field=IntegerField())),
            score_3_count=Count(Case(When(reviews__score=3, then=1), output_field=IntegerField())),
            score_4_count=Count(Case(When(reviews__score=4, then=1), output_field=IntegerField())),
            score_5_count=Count(Case(When(reviews__score=5, then=1), output_field=IntegerField())),
            comments_count=Count('reviews__comment'), average_score=Avg('reviews__score')
        )
