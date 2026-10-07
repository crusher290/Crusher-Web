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

class CategoryDetailListView(View):

    def get(self, request, slug):
        category = get_object_or_404(ArticleCategory, slug=slug)
        articles = category.articles.all()
        return render(request, "article.html", {
            "category":category,
            "articles":articles
        })

class ArticleContentView(View):

    def get(self, request, slug):
        articles = get_object_or_404(Article, slug=slug)
        return render(request, "articlecontent.html", {
            "articles":articles,
        })

        

