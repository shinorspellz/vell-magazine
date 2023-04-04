from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from roles.models import Role

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete= models.CASCADE)
    #timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # cloudinary host
    img = models.ImageField(
        upload_to="images/", default="../profile_avatar_e38sd0"
    )
    #socials
    bio = models.TextField(blank=True)
    linkedin = models.URLField(max_length=200, null= True, blank= True)
    twitter = models.URLField(max_length=200, null= True, blank= True)
    instagram = models.URLField(max_length=200, null= True, blank= True)
    facebook = models.URLField(max_length=200, null= True, blank= True)
    email = models.EmailField(null= True, blank= True)

    class Meta:
        ordering = ['owner']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)