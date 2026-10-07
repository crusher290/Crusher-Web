from django.db import models


class Projcet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_github_link = models.URLField(blank=True)
    collaborators = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title