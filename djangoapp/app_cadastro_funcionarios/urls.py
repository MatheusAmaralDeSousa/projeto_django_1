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
from django.urls import path, include
from app_cadastro_funcionarios import views
from app_navbar import views as navbar_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('', navbar_views.home, name='home'),
    path('navbar/', include('navbar.urls')), 
    # funcionarios.com
    path('',views.home,name = "home"),
    #funcionarios.com/cadastro
    path('cadastro/',views.cadastro_cliente,name = "cadastro_cliente"),
    # funcionarios.com/funcionarios
    path('listagem_cliente/',views.listagem_cliente,name='listagem_cliente'),
    #funcionarios.com/editar
    path('editar/<int:funcionario_id>/',views.editar_cliente,name= "editar_cliente")
]