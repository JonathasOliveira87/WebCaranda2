from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
    verbose_name = 'Contato'  # Defina o nome que você deseja aparecer no painel administrativo
