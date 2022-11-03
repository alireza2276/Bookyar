from django.contrib import admin
from .models import Book, Comment

admin.site.register(Comment)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'user', 'price']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'book', 'datetime_created', ]

