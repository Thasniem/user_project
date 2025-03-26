from django.urls import path, re_path
from .views import IndexView

app_name = 'user_frontend'

urlpatterns = [
    # Main entry point for React app
    path('', IndexView.as_view(), name='index'),
    
    # Catch all routes to let React Router handle them
    re_path(r'^(?:.*)/?$', IndexView.as_view(), name='catch-all'),
]