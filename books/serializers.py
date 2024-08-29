from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from books.models import Book, Author, Bookmark, Review


class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['comment', 'score']


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'comment', 'score']

    def get_username(self, obj):
        return obj.user.username


class BookDetailSerializer(serializers.ModelSerializer):
    reviews = BookReviewSerializer(many=True)
    comments_count = serializers.IntegerField(read_only=True)
    average_score = serializers.IntegerField(read_only=True)
    user_reviews = serializers.SerializerMethodField()
    score_1_count = serializers.IntegerField(read_only=True)
    score_2_count = serializers.IntegerField(read_only=True)
    score_3_count = serializers.IntegerField(read_only=True)
    score_4_count = serializers.IntegerField(read_only=True)
    score_5_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ['title',
                  'reviews',
                  'user_reviews',
                  'comments_count',
                  'average_score',
                  'score_1_count',
                  'score_2_count',
                  'score_3_count',
                  'score_4_count',
                  'score_5_count']

    def get_user_reviews(self, obj):
        reviews = obj.reviews.select_related('user').all()
        return UserReviewSerializer(reviews, many=True).data


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'bookmark_counts']


class AuthenticatedUserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'bookmark_counts', 'is_bookmarked']
