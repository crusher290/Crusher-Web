from django.shortcuts import render, get_object_or_404
from .models import ArticleCategorie, Article
from django.views import View


class ArticleCategorieListView(View):

    def get(self, request):
        categories = ArticleCategorie.objects.all()
        return render(request, "article.html", {"categories" : categories})


class ArticlesListView(View):


    def get(self, request, slug):
        categories = get_object_or_404(ArticleCategorie, slug=slug)
        articles = Article.objects.all()
        return render(request, "article.html", {
            "categories":categories,
            "articles":articles
        })
