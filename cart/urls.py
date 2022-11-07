from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add/<int:book_id>/', views.add_to_cart_view, name='add_cart'),
    path('remove/<int:book_id>/', views.remove_cart_view, name='remove_cart'),
]