"""
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mainHeader = models.CharField(max_length=255)
    subHeader = models.CharField(max_length=255)
    contentHeader = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", blank=True
    )
    month = 
    """