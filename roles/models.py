from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# from profiles.models import Profile

class Role(models.Model):

    roles = (
        ('AUTHOR', 'Author'),
        ('EDITOR', 'Editor'),
        ('EDITORINCHIEF', 'Editor in Chief'),
        ('SUPERADMIN', 'Super Admin'),
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=roles, null=False, default = "AUTHOR")
    

    class Meta:
        ordering = ["role"]

    # def __str__(self):
    #     return f"{self.owner} has {self.role} permissions"


def create_role(sender, instance, created, **kwargs):
    if created:
        Role.objects.create(owner=instance)


post_save.connect(create_role, sender=User)