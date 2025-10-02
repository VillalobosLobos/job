from django import forms
from django.db import connection

class RutaForm(forms.Form):
    nombre_cliente = forms.CharField(
        label="Nombre completo del cliente",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej. Juan Pérez'
        })
    )

    telefono = forms.CharField(
        label="Teléfono",
        max_length=10,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    calle = forms.CharField(
        label="Calle", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    num_int = forms.CharField(
        label="Num. Int", 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    num_ext = forms.CharField(
        label="Num. Ext", 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    colonia = forms.CharField(
        label="Colonia", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    municipio = forms.CharField(
        label="Municipio/Delegación", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    cp = forms.IntegerField(
        label="CP", 
        required=True, 
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    tipo_entrega = forms.ChoiceField(
        label="Tipo de entrega",
        choices=[],  # se llenará dinámicamente
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    beneficio = forms.CharField(
        label="Beneficio",
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 4,
            'style': 'width: 75%; resize: none;'
        })
    )

    monto = forms.DecimalField(
        label="Monto del beneficio",
        max_digits=15,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ejecutar función SQL para obtener tipos de entrega
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM seleccionar_tipo_de_entrega()")
            resultados = cursor.fetchall()


        # Convertir resultados en tuplas para el ChoiceField
        opciones = [(nombre, nombre) for (nombre,) in resultados]
        opciones.insert(0, ("", "Selecciona una opción"))  # opción vacía inicial

        self.fields['tipo_entrega'].choices = opciones
