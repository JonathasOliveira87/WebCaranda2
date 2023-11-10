from django.urls import path
from . import views

urlpatterns = [
    path('', views.panelUser, name='painel'),
    path('updateEmail/', views.update_email, name='update_email'),
    path('updateCelular/', views.update_phone, name='update_phone'),
    path('updateMorador/', views.update_morar, name='update_morar'),
    path('updateDono/', views.update_dono, name='update_dono'),
    path('updateCasa/', views.update_casa, name='update_casa'),
    path('updateCarro/', views.update_carro, name='update_carro'),
    path('updateMoto/', views.update_moto, name='update_moto'),
    path('updatePet/', views.update_pet, name='update_pet'),
    path('updatePhoto/', views.update_photo, name='update_photo'),

]

