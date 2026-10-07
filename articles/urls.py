from django.urls import path, include
from .views import CategoryListView, CategoryDetailListView, ArticleContentView

app_name = "article"

urlpatterns = [
    path('', CategoryListView.as_view(), name="category-list"),
    path('category/<slug:slug>/', CategoryDetailListView.as_view(), name="category-detail"),
    path('article/<slug:slug>/', ArticleContentView.as_view(), name="article-content")
]

