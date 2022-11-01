from django.urls import path
from . import views


urlpatterns = [
    path('', views.BooksListView.as_view(), name='home'),
    path('books/<int:pk>/', views.BooksDetailView.as_view(), name='books_detail')
]