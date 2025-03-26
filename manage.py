#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import traceback
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_project.settings')
    try:
        logger.info("Initializing Django...")
        from django.core.management import execute_from_command_line
        from django.conf import settings
        
        # Enable debug mode for development
        if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
            logger.info("Starting server in debug mode...")
            os.environ['DJANGO_DEBUG'] = 'True'
            
        # Check Django installation and settings
        try:
            import django
            import psycopg2
            import rest_framework
            
            logger.info("Environment Information:")
            logger.info(f"Django version: {django.get_version()}")
            logger.info(f"Python version: {sys.version}")
            logger.info(f"Settings module: {os.environ['DJANGO_SETTINGS_MODULE']}")
            logger.info(f"Current working directory: {os.getcwd()}")
            logger.info("All required packages loaded successfully")
            
        except Exception as e:
            logger.error(f"Configuration check failed: {e}")
            logger.error(traceback.format_exc())
            
        logger.info("Executing management command...")
        execute_from_command_line(sys.argv)
        
    except ImportError as exc:
        logger.error("\nError: Django installation not found!")
        logger.error("Please check the following:")
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
        logger.error(f"\nUnexpected error occurred: {e}")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == '__main__':
    main()