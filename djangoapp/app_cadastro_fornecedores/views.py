from django.shortcuts import render

from djangoapp.app_cadastro_fornecedores.models import Fornecedores
from .models import Funcionarios

def home(request):
    return render(request,'fornecedores/home.html')

def fornecedores(request):
    #Salvar os dados da tela para o banco de dados
    novo_fornecedor = Fornecedores()
    novo_fornecedor.nome =  request.POST.get("nome")
    novo_fornecedor.email =  request.POST.get("email")
    novo_fornecedor.telefone =  request.POST.get("telefone")
    novo_fornecedor.celular =  request.POST.get("celular")
    novo_fornecedor.cep =  request.POST.get("cep")
    novo_fornecedor.endereco =  request.POST.get("endereco")
    novo_fornecedor.numero =  request.POST.get("numero")
    novo_fornecedor.uf =  request.POST.get("uf")
    novo_fornecedor.save()
    
    #Exibir todos os fornecedores do banco de dados
    fornecedor = {
        'fornecedor' : Fornecedores.objects.all()
    }
    #Retornar os dados para a pagina de listagem de fornecedores
    return render(request, 'fornecedores/fornecedores.html', fornecedor)