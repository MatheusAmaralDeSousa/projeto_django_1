from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True)
    idade = models.IntegerField(null=True)
    cpf = models.CharField(max_length=15, null=True)
    rg = models.CharField(max_length=15, null=True)
    objects = models.Manager()
