from instrument.models import Instrument
from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):
    """
    The bookmark model is related to the User and Instrument model.
    The meta property unique_together prevents a user from bookmarking
    the same instrument more than once.
    """
    instrument = models.ForeignKey(
        Instrument, related_name='bookmarks', on_delete=models.CASCADE
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        unique_together = ['instrument', 'owner']

    def __str__(self):
        return f'{self.owner} {self.instrument}'
