from rest_framework import serializers
from .models import UserProfile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserProfile
        fields="__all__"