
from django import forms
from .models import OrdenCombustible
from .models import UsuarioPolicial
from .models import Dependencia
from .models import Subcircuito
from .models import Vehiculo
from .models import AsignacionSubcircuito
from .models import SolicitudMantenimiento
from .models import MantenimientoPreventivo


class OrdenCombustibleForm(forms.ModelForm):
    class Meta:
        model = OrdenCombustible
        fields = '__all__' 


class UsuarioPolicialForm(forms.ModelForm):
    class Meta:
        model = UsuarioPolicial
        fields = ['nombres', 'apellidos', 'fecha_nacimiento', 
                  'tipo_sangre', 'ciudad_nacimiento', 'telefono_celular', 
                  'rango_grado', 'correo_electronico', 'dependencia', 'subcircuito']
class SubcircuitoForm(forms.ModelForm):
    class Meta:
        model = Subcircuito
        fields = '__all__' 

class AsignacionSubcircuitoForm(forms.ModelForm):
    class Meta:
        model = UsuarioPolicial
        fields = ['subcircuito']  # Asegúrate de que el campo se llame 'subcircuito'
        widgets = {
            'subcircuito': forms.Select()  # o forms.SelectMultiple() si un usuario puede ser asignado a múltiples subcircuitos
        }

dependencia = forms.ModelChoiceField(queryset=Dependencia.objects.all(), required=True)

class Dependenciaform(forms.ModelForm):
    class Meta:
        model = Dependencia
        fields = '__all__' 

class Vehiculoform (forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__' 

class SolicitudMantenimientoForm(forms.ModelForm):
    class Meta:
        model = SolicitudMantenimiento
        fields = ['Usuario_Policial', 'Vehiculo', 'fecha_hora', 'kilometraje_actual', 'observaciones']

class MantenimientoPreventivoForm(forms.ModelForm):
    class Meta:
        model = MantenimientoPreventivo
        fields = ['Vehiculo', 'Usuario_Policial', 'fecha_hora_ingreso', 'kilometraje_actual', 'tipo_mantenimiento', 'subtotal', 'iva', 'total', 'imagen_parte_policial']


class ReporteForm(forms.Form):
    TIPO_REPORTE_CHOICES = (
        ('actual', 'Actual'),
        ('historico', 'Histórico'),
    )
    MODELO_CHOICES = (
        ('usuario_policial', 'Usuario Policial'),
        ('solicitud_mantenimiento', 'Solicitud Mantenimiento'),
        # Añade más modelos aquí si es necesario
    )

    tipo_reporte = forms.ChoiceField(choices=TIPO_REPORTE_CHOICES)
    modelo = forms.ChoiceField(choices=MODELO_CHOICES)
    fecha_inicio = forms.DateField(required=False)
    fecha_fin = forms.DateField(required=False)