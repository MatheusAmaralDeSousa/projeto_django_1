from django import forms
from .models import Usuario  # Importe seu modelo de usuário

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'cpf', 'rg']
