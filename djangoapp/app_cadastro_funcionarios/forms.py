from django import forms
from .models import Funcionario
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

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

    # Validação de RG
    def clean_rg(self):
        rg = self.cleaned_data.get('rg')
        if not rg.isdigit() or len(rg) != 9:
            raise ValidationError('RG inválido. Deve conter apenas números e ter 9 dígitos.')
        return rg


    # Validação de e-mail
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_validator = EmailValidator('E-mail inválido.')
        email_validator(email)
        return email

    # Validação de telefone
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone.isdigit() or len(telefone) < 9:
            raise ValidationError('Telefone inválido. Deve conter apenas números e ter pelo menos 9 dígitos.')
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
    
    # Validação de idade
    def clean_idade(self):
        idade = self.cleaned_data.get('idade')
        if idade < 18 or idade > 125:
            raise ValidationError('A idade deve ser maior ou igual a 18 anos.')
        return idade

    # Validação de CPF
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValidationError('CPF inválido. Deve conter apenas números e ter 11 dígitos.')
        return cpf
    
    # Validação de RG
    def clean_rg(self):
        rg = self.cleaned_data.get('rg')
        if not rg.isdigit() or len(rg) != 9:
            raise ValidationError('RG inválido. Deve conter apenas números e ter 9 dígitos.')
        return rg

    # Validação de e-mail
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_validator = EmailValidator('E-mail inválido.')
        email_validator(email)
        return email

    # Validação de telefone
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone.isdigit() or len(telefone) < 9:
            raise ValidationError('Telefone inválido. Deve conter apenas números e ter pelo menos 9 dígitos.')
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
