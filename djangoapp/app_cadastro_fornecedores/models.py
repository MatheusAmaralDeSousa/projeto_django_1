from django.db import models

class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cnpj = models.IntegerField(max_length=14, unique=True)
    email = models.EmailField(max_length=255)
    telefone = models.IntegerField(max_length=11)
    celular = models.IntegerField(max_length=11)
    cep = models.IntegerField(max_length=8)
    endereco = models.CharField(max_length=255)  # Changed from 'endereço'
    numero = models.IntegerField(max_length=10)
    UF = models.CharField(max_length=2)  # Changed from 'UF'
    objects = models.Manager()
