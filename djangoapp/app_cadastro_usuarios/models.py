from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False)
    idade = models.IntegerField(null=False)
    cpf = models.IntegerField(null=False)
    rg = models.IntegerField(null=False)
    objects = models.Manager()