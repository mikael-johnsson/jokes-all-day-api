from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    """
    Follower Model
    Owner is a user that follows another User
    Followed is a user that is followed by Owner
    Unique together makes sure a User can't follow another 
    User twice
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followed"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f"{self.owner} follows {self.followed}"


