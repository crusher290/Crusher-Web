from django.urls import path, include
from .views import ArticlesHomePageView, CategoryArticlesListView

app_name = "article"

urlpatterns = [
    path("", ArticlesHomePageView.as_view(), name="category_list"),
    path('category/<slug:category_slug>/', CategoryArticlesListView.as_view(), name="category_detail")
]   
