from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import ArticleCategory, Article
from django.views import View
from django.views.generic import ListView, DetailView


class ArticlesHomePageView(View):

    def get(self, request):
        categories = ArticleCategory.objects.all()
        return render(request, "category.html", {"categories":categories})

class CategoryArticlesListView(ListView):
    model = Article
    template_name = 'category.html' 
    context_object_name = 'articles'

    def get_queryset(self) -> QuerySet[Any, Any]:

        category_slug = self.kwargs["category_slug"]

        self.category = ArticleCategory.objects.get(slug=category_slug)

        return Article.objects.filter(category=self.category).select_related("category")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)

        context["current_category"] = self.category

        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article.html"
    context_object_name = "article"

    slug_url_kwarg = "article_slug"





