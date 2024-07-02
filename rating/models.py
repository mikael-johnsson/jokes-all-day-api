from django.db import models
from django.contrib.auth.models import User
from joke.models import Joke


class Rating(models.Model):
    """
    Rating model
    Unique together makes sure a user can't
    rate the same joke more than once
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    joke = models.ForeignKey(
        Joke, on_delete=models.CASCADE, related_name="rating"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()

    class Meta:
        ordering = ['-created_at']
        unique_together = ['author', 'joke']

    def __str__(self):
        return f"{self.author}'s rating of: {self.joke.title}"
