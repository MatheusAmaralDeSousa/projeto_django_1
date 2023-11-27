from django import forms
from .models import Fornecedor
from django.core.validators import EmailValidator, RegexValidator

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "cnpj", "email", "telefone", "celular", "cep", "endereco", "numero", "UF"]


    cnpj = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{14}$', message='O CNPJ deve conter exatamente 14 dígitos.')]
    )

    email = forms.CharField(
        validators=[EmailValidator(message='Informe um endereço de e-mail válido.')]
    )

    telefone = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{9,11}$', message='Informe um número de telefone válido.')]
    )
    
    celular = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{9,11}$', message='Informe um número de celular válido.')]
    )

    cep = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{8}$', message='O CEP deve conter exatamente 8 dígitos.')]
    )

    numero = forms.IntegerField()
    
    UF = forms.CharField(
        validators=[RegexValidator(regex=r'^[A-Za-z]{2}$', message='A UF deve conter exatamente 2 letras.')]
    )

class FornecedorEditForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "cnpj", "email", "telefone", "celular", "cep", "endereco", "numero", "UF",]

    cnpj = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{14}$', message='O CNPJ deve conter exatamente 14 dígitos.')]
    )

    email = forms.CharField(
        validators=[EmailValidator(message='Informe um endereço de e-mail válido.')]
    )

    telefone = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{9,11}$', message='Informe um número de telefone válido.')]
    )
    
    celular = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{9,11}$', message='Informe um número de celular válido.')]
    )

    cep = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{8}$', message='O CEP deve conter exatamente 8 dígitos.')]
    )

    numero = forms.IntegerField()
    
    UF = forms.CharField(
        validators=[RegexValidator(regex=r'^[A-Za-z]{2}$', message='A UF deve conter exatamente 2 letras.')]
    )