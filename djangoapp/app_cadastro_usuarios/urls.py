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
from app_cadastro_usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    # usuarios.com/cadastro
    path('usuarios/cadastro/', views.cadastro_cliente, name="cadastro_cliente"),
    # usuarios.com/listagem_cliente
    path('usuarios/listagem_cliente/', views.listagem_cliente, name='listagem_cliente'),
    # usuarios.com/editar
    path('usuarios/editar/<int:usuario_id>/', views.editar_cliente, name="editar_cliente")
]
