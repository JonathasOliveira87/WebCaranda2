from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.contact, name='contato'),
]
