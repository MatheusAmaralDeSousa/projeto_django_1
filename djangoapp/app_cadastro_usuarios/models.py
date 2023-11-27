from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True)
    idade = models.IntegerField(null=True)
    cpf = models.CharField(max_length=11, null=True, unique=True)
    rg = models.CharField(max_length=9, null=True, unique=True)
    email = models.EmailField(max_length=255, null=True)
    telefone = models.CharField(max_length=11, null=True)  
    cep = models.CharField(max_length=8, null=True)  
    endereco = models.CharField(max_length=100, null=True) 
    numero = models.CharField(max_length=8, null=True) 
    bairro = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    complemento = models.CharField(max_length=100, null=True) 
    UF = models.CharField(max_length=2, null=True)  
    objects = models.Manager()