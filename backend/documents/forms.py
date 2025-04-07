from django import forms
from .models import Empleado, Documento

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'empresa']

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['empleado', 'tipo', 'archivo', 'fecha_vencimiento', 'validado']
