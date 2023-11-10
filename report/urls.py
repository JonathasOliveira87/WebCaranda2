from django.urls import path
from . import views


urlpatterns = [
    path('', views.report, name='boletim'),
    path('upload/<int:file_id>/', views.download_file, name='download_file'),
]
