from django.apps import AppConfig


class ReportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'report'
    verbose_name = 'Boletim'  # Defina o nome que você deseja aparecer no painel administrativo
