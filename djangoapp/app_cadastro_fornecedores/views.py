from django.shortcuts import render,  get_object_or_404, redirect
from .models import Fornecedor
from .forms import FornecedorForm, FornecedorEditForm

def home_cadastro_fornecedor(request):
    return render(request, 'home/home.html')


def cadastro_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('listagem_fornecedor')
    else:
        form = FornecedorForm()

    return render(request, 'fornecedores/cadastro_fornecedor.html', {'form': form})


def listagem_fornecedor(request):
    #Exibir todos os fornecedores do banco de dados
    fornecedores = {
        'fornecedores' : Fornecedor.objects.all().order_by('id_fornecedor')
    }
    #Retornar os dados para a pagina de listagem de fornecedores
    return render(request, 'fornecedores/listagem_fornecedor.html', fornecedores)



def editar_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id_fornecedor=fornecedor_id)  

    if request.method == 'POST':
        form = FornecedorEditForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('listagem_fornecedor')
    else:
        form = FornecedorEditForm(instance=fornecedor) 

    return render(request, 'fornecedores/editar_fornecedor.html', {'form': form, 'fornecedor_id': fornecedor_id})


def delete_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, pk=fornecedor_id)
    fornecedor.delete()
    return redirect('listagem_fornecedor')