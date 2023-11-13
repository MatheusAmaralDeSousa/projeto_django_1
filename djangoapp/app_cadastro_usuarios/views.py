from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Usuario

def home(request):
    return render(request, 'home/home.html')

def cadastro_cliente(request):
    return render(request,'usuarios/cadastro_cliente.html')

def listagem_cliente(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome =  request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
    novo_usuario.cpf = request.POST.get("cpf")
    novo_usuario.rg = request.POST.get("rg")
    novo_usuario.save()
    
    #Exibir todos os usuarios do banco de dados
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    #Retornar os dados para a pagina de listagem de usuários
    return render(request, 'usuarios/listagem_cliente.html', usuarios)

#class UsuarioUpdate(UpdateView):
    teplate_name = "cadastro_cliente/forms.html"
    model = "Usuario"
    fields = ["nome", "idade", "cpf", "rg"]
    sucess_url = reverse_lazy("listagem_cliente")
    