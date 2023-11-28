from django import forms
from .models import Fornecedor
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "cnpj", "email", "telefone", "cep", "endereco", "numero", "UF"]

    # Validação de CNPJ
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if not cnpj.isdigit() or len(cnpj) != 14:
            raise ValidationError('CNPJ inválido. Deve conter apenas números e ter 14 dígitos.')
        return cnpj

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
    
class FornecedorEditForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "cnpj", "email", "telefone", "cep", "endereco", "numero", "UF",]

    # Validação de CNPJ
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if not cnpj.isdigit() or len(cnpj) != 14:
            raise ValidationError('CNPJ inválido. Deve conter apenas números e ter 14 dígitos.')
        return cnpj

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