from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import UsuarioForm, LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['Usuario']
            password = form.cleaned_data['Senha  ']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  

    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

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
    usuarios = {
        'usuarios': Usuario.objects.all().order_by('id_usuario')
    }
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
