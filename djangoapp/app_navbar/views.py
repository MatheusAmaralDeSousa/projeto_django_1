from django.shortcuts import render

# Create your views here.
# navbar/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'navbar/home.html')

def cadastro_cliente(request):
    return render(request, 'navbar/cadastro_cliente.html')

def cadastro_funcionario(request):
    return render(request, 'navbar/cadastro_funcionario.html')
