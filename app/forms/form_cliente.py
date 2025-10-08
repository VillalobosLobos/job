from django.core.validators import RegexValidator
from django import forms

class Crear_cliente(forms.Form):
    nombre = forms.CharField(
        label = "Nombre ", 
        max_length = 100, 
        required = True, 
        widget=forms.TextInput(attrs={'title': 'Nombre completo del cliente'}))
    telefono = forms.CharField(
        label = "Telefono ", 
        max_length = 15, 
        validators = [RegexValidator(r'^\+?\d{10,13}$', message="Número de teléfono inválido")],
        widget=forms.TextInput(attrs={'title': 'Ingrese un número de telefono válido'}),
        required = True)