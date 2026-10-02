from django.urls import path, include
from .views import ArticleCategorieListView, ArticlesListView

app_name = "article"

urlpatterns = [
    path("", ArticleCategorieListView.as_view(), name="category_list"),
    path("category/<slug:slug>/", ArticlesListView.as_view(), name="category_detail")
]
