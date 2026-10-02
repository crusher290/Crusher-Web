from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class SkillValue(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="skills")
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.value