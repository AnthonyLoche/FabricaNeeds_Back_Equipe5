from django.apps import AppConfig

class FabricaneedsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.fabricaNeeds'

    def ready(self):
        import core.fabricaNeeds.signals