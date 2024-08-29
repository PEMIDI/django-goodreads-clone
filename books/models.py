from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from utils.base_model import BaseModel

CustomUser = get_user_model()


class Book(BaseModel):
    """ 📕 """
    title = models.CharField(max_length=200, verbose_name=_('title'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'))
    summary = models.TextField(max_length=1000, verbose_name=_('summary'))
    year = models.DateField(verbose_name=_('year of publication'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _('book')
        verbose_name_plural = _('books')

    def bookmark_counts(self):
        return self.bookmarks.count()

    def is_bookmarked(self, user):
        return self.bookmarks.filter(user=user).exists()


class Author(BaseModel):
    """ 🖋 """
    first_name = models.CharField(max_length=150, verbose_name=_('first name'))
    last_name = models.CharField(max_length=150, verbose_name=_('last name'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('book'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('author'))


class Review(BaseModel):
    """ ⭐️⭐️⭐️⭐️⭐️ """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('book'), related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('user'), related_name='reviews')
    comment = models.TextField(max_length=1000, verbose_name=_('comment'), blank=True)
    score = models.IntegerField(
        verbose_name=_('score'),
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, default=0
    )

    def __str__(self):
        return f"{self.book} - {self.user}"

    class Meta:
        unique_together = (("book", "user"),)
        verbose_name = _('review')
        verbose_name_plural = _('reviews')


class Bookmark(BaseModel):
    """ 🔖 """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, verbose_name=_('book'),
                             related_name='bookmarks')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, verbose_name=_('user'),
                             related_name='bookmarks')

    def __str__(self):
        return f"{self.book} - {self.user}"

    class Meta:
        unique_together = (("book", "user"),)
