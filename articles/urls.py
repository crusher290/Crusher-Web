from django.urls import path, include
from .views import CategoryListView

app_name = "article"

urlpatterns = [
    path('', CategoryListView.as_view(), name="category-list"),
    
]

