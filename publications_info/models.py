from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

class PublicationsInfo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    status = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.owner}'s publication info: {self.status} | {self.month} | {self.date}"
