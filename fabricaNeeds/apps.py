from django.apps import AppConfig

class FabricaneedsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fabricaNeeds'

    def ready(self):
        import fabricaNeeds.signals