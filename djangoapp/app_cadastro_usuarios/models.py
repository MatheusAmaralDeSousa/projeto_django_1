from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True)
    idade = models.IntegerField(null=True)
    cpf = models.CharField(max_length=15, null=True)
    rg = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=False)
    telefone = models.CharField(max_length=11, null=False)  
    cep = models.CharField(max_length=8, null=False)  
    endereco = models.CharField(max_length=100, null=False) 
    numero = models.CharField(max_length=5, null=False) 
    bairro = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    complemento = models.CharField(max_length=100, null=False) 
    UF = models.CharField(max_length=2, null=False)  
    objects = models.Manager()
