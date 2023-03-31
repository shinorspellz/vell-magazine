from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mainHeader = models.CharField(max_length=255)
    subHeader = models.CharField(max_length=255)
    contentHeader = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", blank=True
    )
    #topic = models.ManyToManyField(Topics)
    theme = models.CharField(max_length=255)
    template = models.IntegerField()
    # Time stamp for Creative Pool reference.
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # Only Editor in chief + Admin can assign
    """
    status = models.CharField(max_length=255, default="Creative Pool")
    month = models.CharField(max_length=255, default="", blank=True, null=True)
    date =  models.DateTimeField(null=True)
    """

# Is there a cleaner way of sorting the templates? 
# Could we have one stardard template?

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.owner}'s article: {self.mainHeader}"