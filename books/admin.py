from django.contrib import admin
from .models import Book, Author, BookAuthor, Review, Bookmark


class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class BookmarkInline(admin.TabularInline):
    model = Bookmark
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'year', 'get_authors')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BookAuthorInline, ReviewInline, BookmarkInline]

    def get_authors(self, obj):
        return ", ".join([str(author.author) for author in obj.bookauthor_set.all()])

    get_authors.short_description = 'Authors'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
    list_filter = ('book', 'author')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'score', 'comment')
    list_filter = ('book', 'user', 'score')
    search_fields = ('comment',)


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('book', 'user')
    list_filter = ('book', 'user')
