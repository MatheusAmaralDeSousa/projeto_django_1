from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionario
from .forms import FuncionarioForm, FuncionarioEditForm

def home(request):
    return render(request, 'home/home.html')

def cadastro_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_funcionario')
    else:
        form = FuncionarioForm()

    return render(request, 'funcionarios/cadastro_funcionario.html', {'form': form})

def listagem_funcionario(request):
    funcionarios = {
        'funcionarios': Funcionario.objects.all().order_by('id_funcionario')
    }
    return render(request, 'funcionarios/listagem_funcionario.html', funcionarios)

def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id_funcionario=funcionario_id)

    if request.method == 'POST':
        form = FuncionarioEditForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('listagem_funcionario')
    else:
        form = FuncionarioEditForm(instance=funcionario)

    return render(request, 'funcionarios/editar_funcionario.html', {'form': form, 'funcionario_id': funcionario_id})

def delete_user(request, funcionario_id):
    usuario = get_object_or_404(Funcionario, pk=funcionario_id)
    usuario.delete()
    return redirect('listagem_funcionario')