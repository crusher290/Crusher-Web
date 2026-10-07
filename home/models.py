from django.db import models
from .choice import SocialType

class Skill(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class SkillValue(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="skills")
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.value

class Resume(models.Model):
    title = models.CharField(max_length=100, default="Resume")
    file = models.FileField(upload_to="resume/")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class SocialLink(models.Model):
    title = models.CharField(max_length=100)
    vleu = models.CharField(max_length=100)
    kind = models.CharField(choices=SocialType.choices)
    order = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
    
    def __str__(self) -> str:
        return self.title
    