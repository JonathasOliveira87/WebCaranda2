from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('contact.urls')),
    path('register/', views.registration, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('', include('survey.urls')),
    path('', include('report.urls')),
]
