from django.urls import path
from app_cadastro_fornecedores import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    # fornecedores.com
    path('',views.home_fornecedor,name = "home_fornecedor"),
    #fornecedores.com/cadastro
    path('cadastro/',views.cadastro_fornecedor,name = "cadastro_fornecedor"),
    # fornecedores.com/fornecedores
    path('listagem_fornecedores/',views.listagem_fornecedor,name='listagem_fornecedor'),
    #fornecedores.com/editar
    path('editar/<int:fornecedor_id>/',views.editar_fornecedor,name= "editar_fornecedor"),
    #fornecedores/excluir
    path('delete_fornecedor/<int:fornecedor_id>/',views.delete_fornecedor, name='delete_fornecedor')
    
]
