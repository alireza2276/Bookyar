from django.contrib import admin
from .models import Book, Comment, Category
from jalali_date.admin import ModelAdminJalaliMixin
admin.site.register(Comment)
admin.site.register(Category)


@admin.register(Book)
class BookAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'author', 'user', 'price']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'book', 'datetime_created', ]

