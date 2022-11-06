from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=50)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('categories')


class Book(models.Model):
    title = models.CharField(_('title'), max_length=50)
    author = models.CharField(_('author'), max_length=50)
    category = models.ManyToManyField(Category, related_name='categories', verbose_name=_('category'))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'),)
    image = models.ImageField(_('image'), upload_to='images/books')
    translation = models.CharField(_('translation'), max_length=50, null=True, blank=True)
    publication = models.CharField(_('publication'), max_length=50, null=True, blank=True)
    price = models.PositiveIntegerField(_('price'), null=True, blank=True)
    discount = models.PositiveIntegerField(_('discount'), null=True, blank=True)
    status = models.BooleanField(_('status'), default=True)
    fantastic_discount = models.BooleanField(_('fantastic_discount'), default=False)
    description = models.TextField(_('description'))

    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now=True)

    def get_absolute_url(self):
        return reverse('books_detail', args=[self.id])

    def __str__(self):
        return f"{self.title} - {self.user}"

    class Meta:
        verbose_name_plural = _('books')


class Comment(models.Model):
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField()
    description = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.book}"

    class Meta:
        verbose_name_plural = _('comments')

