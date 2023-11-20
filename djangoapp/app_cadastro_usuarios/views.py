from django.shortcuts import render,  get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm

def home(request):
    return render(request, 'home/home.html')


def cadastro_cliente(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('listagem_cliente')
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/cadastro_cliente.html', {'form': form})


def listagem_cliente(request):
    #Exibir todos os usuarios do banco de dados
    usuarios = {
        'usuarios' : Usuario.objects.all().order_by('id_usuario')
    }
    #Retornar os dados para a pagina de listagem de usuários
    return render(request, 'usuarios/listagem_cliente.html', usuarios)



def editar_cliente(request, id):
    usuario = get_object_or_404(Usuario, pk=id) 

    if request.method == 'POST':
        usuario.nome = request.POST.get("nome")
        usuario.idade = request.POST.get("idade")
        usuario.cpf = request.POST.get("cpf")
        usuario.rg = request.POST.get("rg")
        usuario.save()  

        return redirect('listagem_cliente')

    return render(request, 'usuarios/editar_cliente.html', {'usuario': usuario})
