from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario  # Importe seu modelo de usuário

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha  '}))

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'cpf', 'rg']



