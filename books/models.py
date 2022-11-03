from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/books')
    translation = models.CharField(max_length=50, null=True, blank=True)
    publication = models.CharField(max_length=50, null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    description = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('books_detail', args=[self.id])

    def __str__(self):
        return f"{self.title} - {self.user}"


class Comment(models.Model):
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField()
    description = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.book}"

