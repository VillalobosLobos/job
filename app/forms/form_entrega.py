from django import forms

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