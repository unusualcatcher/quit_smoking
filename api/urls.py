from django.urls import path, include
from api.views import UserProfileViewSet, ReasonForSmokingViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'smoking-reasons', ReasonForSmokingViewSet)

urlpatterns = [
    path('', include(router.urls))

]