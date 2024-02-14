from django.contrib import admin
from policia1loja.models import Dependencia
from .models import OrdenCombustible
from .models import Vehiculo
from .models import UsuarioPolicial

admin.site.register(Vehiculo)
admin.site.register(OrdenCombustible)
admin.site.register(Dependencia)
admin.site.register(UsuarioPolicial)