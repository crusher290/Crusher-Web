from django.urls import path, include
from .views import CategoryListView, CategoryDetailListView, ArticleContentView

app_name = "article"

urlpatterns = [
    #================================= with this view client can see the category of articles
    path('', CategoryListView.as_view(), name="category-list"),
    #================================= with this view client can see the article that blong the category
    path('category/<slug:slug>/', CategoryDetailListView.as_view(), name="category-detail"),
    #================================= with this view client can see the content of the article
    path('article/<slug:slug>/', ArticleContentView.as_view(), name="article-content")
    #=================================
]

