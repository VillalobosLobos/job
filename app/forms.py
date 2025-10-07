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

class Crear_entrega(forms.Form):
    tipo_de_entrega = forms.ChoiceField(
        choices = [('', 'Seleccione una opción'), ('campo', 'Campo'), ('masivo', 'Masivo')],
        required = True
    )
    beneficios = forms.CharField(
        label = "Beneficios ", 
        max_length = 100, 
        widget = forms.Textarea,
        required = True)
    monto = forms.DecimalField(
        max_digits = 15,
        decimal_places = 2,
        widget=forms.TextInput(attrs={'title': 'Ingrese el monto para el beneficio'}),
        min_value = 0.0
    )