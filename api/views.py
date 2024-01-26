from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile
from .serializers import ProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=ProfileSerializer
    
