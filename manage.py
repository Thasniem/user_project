#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import traceback
import logging
import time
from pathlib import Path

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(name)s:%(lineno)d] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('django_debug.log')
    ]
)
logger = logging.getLogger(__name__)

def check_environment():
    """Check environment setup and dependencies."""
    env_info = {
        'Python Version': sys.version,
        'Python Path': sys.executable,
        'Working Directory': os.getcwd(),
        'PYTHONPATH': os.environ.get('PYTHONPATH', 'Not Set'),
        'DJANGO_SETTINGS_MODULE': os.environ.get('DJANGO_SETTINGS_MODULE', 'Not Set'),
        'Virtual Environment': os.environ.get('VIRTUAL_ENV', 'Not Active'),
        'Installed Packages': []
    }
    
    # Check installed packages
    try:
        import pkg_resources
        env_info['Installed Packages'] = [
            f"{dist.key} ({dist.version})"
            for dist in pkg_resources.working_set
        ]
    except ImportError:
        env_info['Installed Packages'] = ['pkg_resources not available']
    
    for key, value in env_info.items():
        if key == 'Installed Packages':
            logger.debug(f"{key}:")
            for pkg in value:
                logger.debug(f"  - {pkg}")
        else:
            logger.debug(f"{key}: {value}")
    
    return env_info

def check_django_installation():
    """Verify Django installation and dependencies."""
    try:
        import django
        logger.info(f"Django is installed (version {django.get_version()})")
        return True
    except ImportError:
        logger.error("Django import failed!")
        return False

def main():
    """Run administrative tasks."""
    start_time = time.time()
    logger.info("Starting Django management script...")
    
    try:
        # Set default settings module
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_project.settings')
        
        # Check environment before proceeding
        env_info = check_environment()
        
        # Verify Django installation
        if not check_django_installation():
            raise ImportError("Django not found in the current environment")
        
        logger.info("Initializing Django...")
        from django.core.management import execute_from_command_line
        from django.conf import settings
        
        # Enable debug mode for development
        if len(sys.argv) > 1:
            logger.info(f"Command being executed: {' '.join(sys.argv[1:])}")
            if sys.argv[1] == 'runserver':
                logger.info("Starting server in debug mode...")
                os.environ['DJANGO_DEBUG'] = 'True'
        
        # Check Django installation and settings
        try:
            import django
            import psycopg2
            import rest_framework
            
            logger.info("Required packages check:")
            logger.info(f"Django version: {django.get_version()}")
            logger.info(f"PostgreSQL adapter: {psycopg2.__version__}")
            logger.info(f"REST framework: {rest_framework.VERSION}")
            
            # Check database configuration
            db_settings = settings.DATABASES.get('default', {})
            logger.info(f"Database engine: {db_settings.get('ENGINE', 'Not configured')}")
            logger.info(f"Database name: {db_settings.get('NAME', 'Not configured')}")
            
            # Check installed apps
            logger.info("Installed apps:")
            for app in settings.INSTALLED_APPS:
                logger.info(f"  - {app}")
            
        except Exception as e:
            logger.error("Configuration check failed!")
            logger.error(f"Error type: {type(e).__name__}")
            logger.error(f"Error message: {str(e)}")
            logger.error(traceback.format_exc())
            raise
        
        logger.info("Executing management command...")
        execute_from_command_line(sys.argv)
        
    except ImportError as exc:
        logger.critical("Django installation not found!")
        logger.error("Environment check results:")
        check_environment()
        logger.error("\nPlease verify:")
        logger.error("1. Django is installed (pip install django)")
        logger.error("2. Virtual environment is activated (if using one)")
        logger.error("3. PYTHONPATH is correctly set")
        logger.error("\nDetailed error:")
        logger.error(traceback.format_exc())
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    except Exception as e:
        logger.critical(f"Unexpected error occurred: {type(e).__name__}")
        logger.critical(f"Error message: {str(e)}")
        logger.error(traceback.format_exc())
        sys.exit(1)
    finally:
        execution_time = time.time() - start_time
        logger.info(f"Script execution completed in {execution_time:.2f} seconds")

if __name__ == '__main__':
    main()