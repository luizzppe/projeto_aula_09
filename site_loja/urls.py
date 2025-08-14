# site_loja/urls.py

from django.urls import path
from . import views

app_name = 'site_loja' # Define um namespace para suas URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('perfil/', views.perfil, name='perfil'), # URL para a página de perfil
]