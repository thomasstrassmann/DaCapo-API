from django.db import models
from django.contrib.auth.models import User


class Wanted(models.Model):
    """
    The Wanted Model is related to the owner model.
    It holds all the relevant data to present the items wanted
    by several users.
    """
    category_choices = [
        ('guitar', 'Guitar'), ('bass', 'Bass'), ('drums', 'Drums'),
        ('piano', 'Piano'), ('brass instruments', 'Brass instruments'),
        ('other', 'Other')]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False,
                             blank=False)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=category_choices,
                                default='guitar')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.title} by {self.owner}'
