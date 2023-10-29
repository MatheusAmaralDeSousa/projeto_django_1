from django.db import models

class Funcionarios(models.Model):
    id_Funcionarios = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False)
    email = models.TextField(max_length=255, null=False)
    celular = models.IntegerField(null=False)
    cep = models.IntegerField(null=False)
    endereco = models.TextField(max_length=255, null=False)
    numero = models.IntegerField(null=False)
    idade = models.IntegerField(null=False)
    uf = models.TextField(max_length=255, null=False)
    cpf = models.IntegerField(null=False)
    rg = models.IntegerField(null=False)
    cargo = models.TextField(max_length=255, null=False)
    objects = models.Manager()