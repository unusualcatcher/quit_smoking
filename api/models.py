from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    streak = models.PositiveIntegerField(default=0)
    reason_for_smoking = models.CharField(max_length=255, blank=True, null=True)
    smoked_today = models.BooleanField(default=False)
    # profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    listened_to_hypnotune_today = models.BooleanField(default=False)
    total_hypnotunes_listened = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.user.username