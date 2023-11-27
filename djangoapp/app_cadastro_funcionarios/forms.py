from django import forms
from .models import Funcionario
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator
from django.forms import ModelForm

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ["nome", "idade", "cpf", "rg", "email", "telefone", "cep", "endereco", "bairro", "cidade", "complemento", "numero", "uf", "cargo"]
    
    # Validação de idade
    def clean_idade(self):
        idade = self.cleaned_data.get('idade')
        if idade < 18:
            raise ValidationError('A idade deve ser maior ou igual a 18 anos.')
        return idade

    # Validação de CPF
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValidationError('CPF inválido. Deve conter apenas números e ter 11 dígitos.')
        return cpf

    # Validação de e-mail
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_validator = EmailValidator('E-mail inválido.')
        email_validator(email)
        return email

    # Validação de telefone
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone.isdigit() or len(telefone) < 10:
            raise ValidationError('Telefone inválido. Deve conter apenas números e ter pelo menos 10 dígitos.')
        return telefone

    # Validação de CEP
    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if not cep.isdigit() or len(cep) != 8:
            raise ValidationError('CEP inválido. Deve conter apenas números e ter 8 dígitos.')
        return cep

    # Validação de número
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise ValidationError('Número inválido. Deve conter apenas números.')
        return numero

class FuncionarioEditForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ["nome", "idade", "cpf", "rg", "email", "telefone", "cep", "endereco", "bairro", "cidade", "complemento", "numero", "uf", "cargo"]
    
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
        validators=[RegexValidator(regex=r'^\d{10,11}$', message='Informe um número de telefone válido.')]
    )

    cep = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{8}$', message='O CEP deve conter exatamente 8 dígitos.')]
    )

    numero = forms.IntegerField(
        validators=[RegexValidator(regex=r'^[0-9]*$', message='Apenas números são permitidos.')]
    )