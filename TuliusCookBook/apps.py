from django.apps import AppConfig


class TuliuscookbookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TuliusCookBook'

    def ready(self):
        import TuliusCookBook.signals
