from django.db import transaction
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Count, Exists, OuterRef, Avg, Case, When, IntegerField
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet

from books.models import Book, Bookmark, Review
from books.paginations import BookStandardPagination
from books.serializers import BookSerializer, AuthenticatedUserBookSerializer, BookDetailSerializer, AddReviewSerializer


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


class RetrieveBookViewSet(RetrieveModelMixin, GenericViewSet):
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

    @action(detail=True, methods=['post'], url_path='bookmark')
    def add_to_bookmarks(self, request, pk=None):
        book = self.get_object()
        user = request.user

        if book.is_bookmarked(user):
            return Response({"detail": "You have already bookmarked this book."}, status=status.HTTP_400_BAD_REQUEST)

        if book.reviews.filter(user=user).exists():
            return Response({"detail": "You cannot bookmark a book after commenting or scoring."},
                            status=status.HTTP_400_BAD_REQUEST)

        Bookmark.objects.create(book=book, user=user)
        return Response({"detail": "Book bookmarked successfully."}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path='add-review', permission_classes=[permissions.IsAuthenticated])
    def add_review(self, request, pk=None):
        book = self.get_object()
        user = request.user
        serializer = AddReviewSerializer(data=request.data)

        if serializer.is_valid():
            review, created = Review.add_or_update_review(
                book=book,
                user=user,
                comment=serializer.validated_data.get('comment'),
                score=serializer.validated_data.get('score')
            )

            if created:
                return Response({'status': 'review added'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'review updated'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
