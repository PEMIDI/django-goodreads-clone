from rest_framework import serializers

from books.models import Book, Author, Bookmark


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'bookmark_counts']


class AuthenticatedUserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'bookmark_counts', 'is_bookmarked']
