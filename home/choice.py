from django.db import models

class SocialType(models.TextChoices):
    EMAIL = 'email', 'Email'
    PHONE = 'phone', 'Phone'
    LINK = 'link', 'Link'
