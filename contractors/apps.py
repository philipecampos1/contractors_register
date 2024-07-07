from django.apps import AppConfig


class ContractorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contractors'

    def ready(self):
        import contractors.signals
