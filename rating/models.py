from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User


class Rating(models.Model):
    """
    The model relates to User and Profile. With the rating choices, a
    user can rate a profile based on the previous shopping experience.
    """
    rating_choices = [
        ('bad', 'Bad!'), ('average', 'Average!'), ('awesome', 'Awesome!')]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.CharField(max_length=50, choices=rating_choices,
                              default='average')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        unique_together = ['profile', 'owner']

    def __str__(self):
        return f"{self.owner} rates {self.profile} with {self.rating}"
