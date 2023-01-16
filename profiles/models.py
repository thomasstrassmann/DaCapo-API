from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Avg
from rating.models import Rating


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(
        upload_to='images/', default='../default_profile_srtwni'
    )
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def average_rating(self) -> float:
        return Rating.objects.filter(
            profile_id=self).aggregate(Avg('rating'))["rating__avg"] or 0

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Profile of {self.owner}"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
