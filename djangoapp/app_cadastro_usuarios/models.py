from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, null=False)  
    idade = models.IntegerField(null=False)  
    cpf = models.CharField(max_length=11, null=False)  
    rg = models.CharField(max_length=9, null=False)  
    objects = models.Manager()
