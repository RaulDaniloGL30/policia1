import django_filters
from .models import Dependencia

class DependenciaFilter(django_filters.FilterSet):
    class Meta:
        model = Dependencia
        fields = {
            'Provincia': ['icontains'],
            'Numero_distrito': ['icontains'],
            'Parroquia': ['icontains'],
            # Añade aquí otros campos que quieras filtrar
        }