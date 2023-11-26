from django.shortcuts import render,  get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm, UsuarioEditForm

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



def editar_cliente(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)  

    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listagem_cliente')
    else:
        form = UsuarioEditForm(instance=usuario) 

    return render(request, 'usuarios/editar_cliente.html', {'form': form, 'usuario_id': usuario_id})
