from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "cnpj", "email", "telefone", "celular", "cep", "endereco", "numero", "UF",]

class FornecedorEditForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "cnpj", "email", "telefone", "celular", "cep", "endereco", "numero", "UF",]
