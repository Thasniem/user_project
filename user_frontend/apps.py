from django.apps import AppConfig

class UserFrontendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_frontend'
    verbose_name = 'User Frontend'

    def ready(self):
        pass