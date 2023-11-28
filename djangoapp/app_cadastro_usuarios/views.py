from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import UsuarioForm, UsuarioEditForm, LoginForm


@login_required(login_url='login')
def home_cliente(request):
    return render(request, 'home/home_cliente.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['Usuario']
            password = form.cleaned_data['Senha']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

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
    usuarios = {
        'usuarios': Usuario.objects.all().order_by('id_usuario')
    }
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


def delete_user(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    usuario.delete()
    return redirect('listagem_cliente')