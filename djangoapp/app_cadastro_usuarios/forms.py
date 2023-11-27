from django import forms
from .models import Usuario
from django.core.validators import EmailValidator, RegexValidator

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "idade", "cpf", "rg", "email", "telefone", "cep", "endereco", "bairro", "cidade", "complemento", "numero", "UF"]
    
    idade = forms.IntegerField(
        validators=[RegexValidator(regex=r'^[0-9]*$', message='Apenas números são permitidos.')]
    )

    cpf = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{11}$', message='O CPF deve conter exatamente 11 dígitos.')]
    )

    email = forms.CharField(
        validators=[EmailValidator(message='Informe um endereço de e-mail válido.')]
    )

    telefone = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{9,11}$', message='Informe um número de telefone válido.')]
    )

    cep = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{8}$', message='O CEP deve conter exatamente 8 dígitos.')]
    )

    numero = forms.CharField(
        validators=[RegexValidator(regex=r'^[0-9]*$', message='Apenas números são permitidos.')]
    )
    
    UF = forms.CharField(
        validators=[RegexValidator(regex=r'^[A-Za-z]{2}$', message='A UF deve conter exatamente 2 letras.')]
    )

class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "idade", "cpf", "rg", "email", "telefone", "cep", "endereco", "bairro", "cidade", "complemento", "numero", "UF"]
    
    idade = forms.IntegerField(
        validators=[RegexValidator(regex=r'^[0-9]*$', message='Apenas números são permitidos.')]
    )

    cpf = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{11}$', message='O CPF deve conter exatamente 11 dígitos.')]
    )

    email = forms.CharField(
        validators=[EmailValidator(message='Informe um endereço de e-mail válido.')]
    )

    telefone = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{9,11}$', message='Informe um número de telefone válido.')]
    )

    cep = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{8}$', message='O CEP deve conter exatamente 8 dígitos.')]
    )

    numero = forms.CharField(
        validators=[RegexValidator(regex=r'^[0-9]*$', message='Apenas números são permitidos.')]
    )
    
    UF = forms.CharField(
        validators=[RegexValidator(regex=r'^[A-Za-z]{2}$', message='A UF deve conter exatamente 2 letras.')]
    )