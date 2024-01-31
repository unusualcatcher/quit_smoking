from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ReasonForSmoking(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.reason

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    streak = models.PositiveIntegerField(default=0)
    reason_for_smoking = models.ManyToManyField(ReasonForSmoking, blank=True)
    smoked_today = models.BooleanField(default=False)
    # profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    listened_to_hypnotune_today = models.BooleanField(default=False)
    total_hypnotunes_listened = models.PositiveIntegerField(default=0)
    cigerettes_smoked_today = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username