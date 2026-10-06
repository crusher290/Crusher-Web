from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import ArticleCategory, Article
from django.views import View
from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    model = ArticleCategory
    template_name = "category.html"
    context_object_name = "categories"

