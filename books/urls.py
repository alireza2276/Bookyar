from django.urls import path
from . import views


urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', views.book_detail_view, name='books_detail'),
    path('new', views.BooksCreateView.as_view(), name='books_new'),
    path('edit/<int:pk>/', views.BooksUpdateView.as_view(), name='books_edit'),
    path('delete/<int:pk>/', views.BooksDeleteView.as_view(), name='books_delete'),
    path('category/<int:pk>/', views.category, name='category'),
]