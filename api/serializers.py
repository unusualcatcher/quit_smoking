from rest_framework import serializers
from .models import UserProfile, ReasonForSmoking

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserProfile
        fields="__all__"

class ReasonForSmokingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReasonForSmoking
        fields = '__all__'
