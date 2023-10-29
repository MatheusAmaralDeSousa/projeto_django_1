from django.shortcuts import render
from .models import Funcionarios

def home(request):
    return render(request,'funcionarios/home.html')

def funcionarios(request):
    #Salvar os dados da tela para o banco de dados
    novo_funcionario = Funcionarios()
    novo_funcionario.nome =  request.POST.get("nome")
    novo_funcionario.email =  request.POST.get("email")
    novo_funcionario.telefone =  request.POST.get("telefone")
    novo_funcionario.cep =  request.POST.get("cep")
    novo_funcionario.endereco =  request.POST.get("endereco")
    novo_funcionario.numero =  request.POST.get("numero")
    novo_funcionario.uf =  request.POST.get("uf")
    novo_funcionario.idade = request.POST.get("idade")
    novo_funcionario.cpf = request.POST.get("cpf")
    novo_funcionario.rg = request.POST.get("rg")
    novo_funcionario.cargo =  request.POST.get("cargo")
    novo_funcionario.save()
    
    #Exibir todos os funcionarios do banco de dados
    funcionario = {
        'funcionario' : Funcionarios.objects.all()
    }
    #Retornar os dados para a pagina de listagem de usuários
    return render(request, 'funcionario/funcionario.html', funcionario)