from django.db import models
from django.contrib.auth.models import User
from joke.models import Joke


class Report(models.Model):
    """
    Report model
    """
    reason_choices = [
        ('choose_an_option', 'Choose an option'),
        ('racism', 'Racism'),
        ('sexism', 'Sexism'),
        ('inappropriate', 'Inappropriate'),
        ('personal_attack', 'Personal attack')
    ]

    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    joke = models.ForeignKey(
        Joke, on_delete=models.CASCADE
    )
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)
    reason = models.CharField(
        max_length=32, choices=reason_choices, default='Choose an option'
        )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner} reports {self.joke.title}"
