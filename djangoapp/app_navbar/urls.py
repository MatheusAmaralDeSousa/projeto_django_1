# navbar/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro_funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),
    # Adicione outras URLs conforme necessário
]
