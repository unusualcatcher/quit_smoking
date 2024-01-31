from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, ReasonForSmoking
from .serializers import ProfileSerializer, ReasonForSmokingSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=ProfileSerializer

class ReasonForSmokingViewSet(viewsets.ModelViewSet):
    queryset = ReasonForSmoking.objects.all()
    serializer_class = ReasonForSmokingSerializer    

# views.py
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework import status
# from rest_framework import viewsets
# from .models import UserProfile
# from .serializers import ProfileSerializer

# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = ProfileSerializer

#     @action(detail=False, methods=['post'])
#     def create_profile(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         serializer.save()
