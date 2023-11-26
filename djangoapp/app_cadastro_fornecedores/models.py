from django.db import models

class Fornecedores(models.Model):
    id_Fornecedores = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False)
    cnpj = models.IntegerField(null=False)
    email = models.TextField(max_length=255, null=False)
    telefone = models.IntegerField(null=False)
    celular = models.IntegerField(null=False)
    cep = models.IntegerField(null=False)
    endereco = models.TextField(max_length=255, null=False)
    numero = models.IntegerField(null=False)
    uf = models.TextField(max_length=255, null=False)
    objects = models.Manager()