from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "idade", "cpf", "rg"]

class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "idade", "cpf", "rg"]
