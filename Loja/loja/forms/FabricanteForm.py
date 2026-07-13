from django.forms import ModelForm
from django import forms
from loja.models.Usuario import Usuario
from loja.models import Fabricante

class FabricanteForm(ModelForm):
    class Meta:
        model = Fabricante
        fields = ['Fabricante']
        widgets = {
            'Fabricante': forms.TextInput(attrs={'class': "form-control"}),
        }