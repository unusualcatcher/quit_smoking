from django.urls import path, include
from api.views import UserProfileViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))

]