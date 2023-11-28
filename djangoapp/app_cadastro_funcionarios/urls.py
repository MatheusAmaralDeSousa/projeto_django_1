"""
URL configuration for projeto project.

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
from app_cadastro_funcionarios import views


urlpatterns = [
    path('', views.home_funcionario, name="home_funcionario"),
    # funcionarios.com/cadastro
    path('cadastro/', views.cadastro_funcionario, name="cadastro_funcionario"),
    # funcionarios.com/listagem_cliente
    path('listagem_funcionario/', views.listagem_funcionario, name='listagem_funcionario'),
    # funcionarios.com/editar
    path('editar/<int:funcionario_id>/', views.editar_funcionario, name="editar_funcionario"),
    # funcionarios.com/excluir
    path('delete_funcionario/<int:funcionario_id>/',views.delete_funcionario, name='delete_funcionario'),
]
