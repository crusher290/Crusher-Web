from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class ArticleCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.title

class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.PROTECT, related_name="articles")
    name = models.CharField(max_length=100)
    content = CKEditor5Field("Content", config_name="default")
    description = models.TextField()
    collaborators = models.CharField(max_length=100)
    article_creation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name