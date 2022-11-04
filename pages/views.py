from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from books.models import Category


class HomeView(TemplateView):
    template_name = 'pages/home.html'



