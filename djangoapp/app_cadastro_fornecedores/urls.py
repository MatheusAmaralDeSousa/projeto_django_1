"""
URL configuration for projeto_cadastro_usuarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    # usuarios.com
    path('',views.homeCadastro_fornecedor,name = "home"),
    #usuarios.com/cadastro
    path('cadastro/',views.cadastro_fornecedor,name = "cadastro_fornecedor"),
    # usuarios.com/usuarios
    path('listagem_fornecedor/',views.listagem_fornecedor,name='listagem_fornecedor'),
    #usuarios.com/editar
    path('editar/<int:usuario_id>/',views.editar_fornecedor,name= "editar_fornecedor"),
    #usuarios/excluir
    path('delete_user/<int:user_id>/',views.delete_user, name='delete_user'),
]
