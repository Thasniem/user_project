from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
import logging

# Configure logging
logger = logging.getLogger(__name__)

# API Schema configuration
schema_view = get_schema_view(
    title='User Management API',
    description='API for user management system',
    version='1.0.0'
)

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', include('user_app.urls')),
    
    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API authentication
    path('api-auth/', include('rest_framework.urls')),
    
    # API documentation
    path('docs/', include_docs_urls(
        title='User Management API',
        description='API documentation for user management system',
        authentication_classes=[],
        permission_classes=[],
    )),
    
    # API Schema
    path('schema/', schema_view, name='openapi-schema'),
    
    # Frontend URLs
    path('', include('user_frontend.urls')),
    
    # Favicon
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]

# Debug configuration
if settings.DEBUG:
    try:
        # Debug toolbar
        import debug_toolbar
        urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))
        logger.debug("Debug toolbar URLs added successfully")
        
        # Media files
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
        )
        logger.debug(f"Media URLs added: {settings.MEDIA_URL} -> {settings.MEDIA_ROOT}")
        
        # Static files
        urlpatterns += static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
        )
        logger.debug(f"Static URLs added: {settings.STATIC_URL} -> {settings.STATIC_ROOT}")
        
    except ImportError as e:
        logger.warning(f"Debug toolbar import failed: {str(e)}")
    except Exception as e:
        logger.error(f"Error configuring debug URLs: {str(e)}")

# Log all registered URLs in debug mode
if settings.DEBUG:
    logger.debug("Registered URLs:")
    for pattern in urlpatterns:
        logger.debug(f" - {pattern.pattern}")