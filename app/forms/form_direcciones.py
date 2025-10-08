from django.core.validators import RegexValidator
from django import forms

class Crear_direccion(forms.Form):
    calle = forms.CharField(
        label = "Calle ", 
        max_length = 100, 
        widget=forms.TextInput(attrs={'title': 'Ingrese la calle'}),
        required = True)
    numero_exterior = forms.CharField(
        label = "Num. Ext. ", 
        max_length = 100, 
        widget=forms.TextInput(attrs={'title': 'Número exterior del cliente'}),
        required = True)
    numero_interior = forms.CharField(
        label = "Num. Int. ", 
        widget=forms.TextInput(attrs={'title': 'Número interior del cliente'}),
        max_length = 100)
    colonia = forms.CharField(
        label = "Colonia ", 
        max_length = 100, 
        widget=forms.TextInput(attrs={'title': 'Colonia del cliente'}),
        required = True)
    delegacion = forms.CharField(
        label = "Delegación/Municipio ", 
        max_length = 100, 
        widget=forms.TextInput(attrs={'title': 'Ingrese la delegación o municipio'}),
        required = True)
    cp = forms.CharField(
        label = "C.P ", 
        max_length = 5,
        widget=forms.TextInput(attrs={'title': 'Ingrese el código postal del cliente'}),
        validators = [RegexValidator(r'^\d{5}$', message="Código postal inválido")],
        required = True)