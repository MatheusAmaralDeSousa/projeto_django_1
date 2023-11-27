from django.db import models

class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)  # Changed from 'endereço'
    numero = models.CharField(max_length=10)
    UF = models.CharField(max_length=2)  # Changed from 'UF'
    objects = models.Manager()
