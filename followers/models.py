from django.contrib.auth.models import User
from django.db import models


class Follower(models.Model):
    """
    followed_user and following_user are both model instances of User.
    unique_together is necessary to prevent someone to follow the 
    same user twice.
    """
    followed_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed')
    following_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        unique_together = ['following_user', 'followed_user']

    def __str__(self):
        return f'{self.following_user} follows {self.followed_user}'
