from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'user_app'

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'auth', views.AuthViewSet, basename='auth')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'profiles', views.ProfileViewSet, basename='profile')
router.register(r'activity-logs', views.ActivityLogViewSet, basename='activity-log')

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]