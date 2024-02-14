#from django.shortcuts import render
#from .models import UsuarioPolicial


#def lista_usuarios(request):
    #usuarios = UsuarioPolicial.objects.all()
    #return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import OrdenCombustible
from .forms import OrdenCombustibleForm
from django.http import HttpResponse
from .models import UsuarioPolicial
from .forms import UsuarioPolicialForm
from .models import Dependencia
from django.contrib import messages
from .models import Subcircuito
from .forms import SubcircuitoForm
import csv
from django.views.decorators.http import require_POST
from .forms import Dependenciaform
from .models import Vehiculo
from .forms import Vehiculoform
from .forms import AsignacionSubcircuitoForm
from .filters import DependenciaFilter
from .forms import SolicitudMantenimientoForm
from .models import SolicitudMantenimiento
from .forms import MantenimientoPreventivoForm
from .forms import MantenimientoPreventivo
from reportlab.pdfgen import canvas
from .models import MantenimientoPreventivo
from .forms import ReporteForm
from django.utils import timezone
from rest_framework import generics
from .serializers import OrdenCombustibleSerializer





    #Inicio

def inicio(request):
    return render(request, 'policia1loja/inicio.html')

    #----------------------------------------------------------------------------------------------------------Gestion de usuarios
    #Listar Usuarios
def lista_usuarios(request):
     usuarios = UsuarioPolicial.objects.all()
     return render(request, 'policia1loja/lista_usuarios.html', {'usuarios': usuarios})
#--------------------------------------------------------------------------------------------------------------REPORTES------------

def generar_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            tipo_reporte = form.cleaned_data['tipo_reporte']
            modelo_seleccionado = form.cleaned_data['modelo']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']

            # Crear el archivo CSV para el reporte
            response = HttpResponse(content_type='text/csv; charset=utf-8-sig')  # Agregar 'charset=utf-8-sig'
            response['Content-Disposition'] = f'attachment; filename="reporte_{modelo_seleccionado}.csv"'
            writer = csv.writer(response)

            if modelo_seleccionado == 'usuario_policial':
                # Lógica para UsuarioPolicial
                datos = UsuarioPolicial.objects.all()
                if tipo_reporte == 'actual':
                    datos = datos.filter(fecha_nacimiento__gte=timezone.now())
                elif fecha_inicio and fecha_fin:
                    datos = datos.filter(fecha_nacimiento__range=(fecha_inicio, fecha_fin))

                writer.writerow(['Identificacion', 'Nombres', 'Apellidos', 'Fecha Nacimiento', 'Correo Electronico', 'Telefono'])
                for usuario in datos:
                    writer.writerow([
                        usuario.identificacion, 
                        usuario.nombres, 
                        usuario.apellidos, 
                        usuario.fecha_nacimiento, 
                        usuario.correo_electronico, 
                        usuario.telefono_celular
                    ])

            elif modelo_seleccionado == 'solicitud_mantenimiento':
                # Lógica para SolicitudMantenimiento
                datos = SolicitudMantenimiento.objects.all()
                if tipo_reporte == 'actual':
                  datos = datos.filter(fecha_hora__gte=timezone.now())
                elif fecha_inicio and fecha_fin:
                  datos = datos.filter(fecha_hora__range=(fecha_inicio, fecha_fin))
                # Aquí agregar lógica adicional para filtrar SolicitudMantenimiento si es necesario

                # Encabezados para SolicitudMantenimiento
                writer.writerow(['Nombre del Usuario Policial', 'Placa del Vehículo', 'Fecha y Hora', 'Kilometraje Actual', 'Observaciones'])
                for solicitud in datos:
                 writer.writerow([
                    solicitud.Usuario_Policial.nombres,
                    solicitud.Vehiculo.placa,
                    solicitud.fecha_hora,
                    solicitud.kilometraje_actual,
                    solicitud.observaciones
        ])
            
            return response

    else:
        form = ReporteForm()
    
    return render(request, 'policia1loja/generar_reporte.html', {'form': form})




    
    #Crear Usuario 
def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioPolicialForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            dependencia_id = form.cleaned_data.get('dependencia').id  # Obtén el ID de la dependencia
            usuario.dependencia_id = dependencia_id  # Asigna el ID a la clave foránea
            usuario.save()
            messages.success(request, 'Usuario creado con éxito.')
            return redirect('lista_usuarios')
        else:
            # Manejo de errores del formulario
             for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field}: {error}")
    else:
        form = UsuarioPolicialForm()
    return render(request, 'policia1loja/agregar_editar_usuarios.html', {'form': form})


    #Editar usuario
def editar_usuario(request, id):
    usuario = get_object_or_404(UsuarioPolicial, pk=id)
    if request.method == 'POST':
        form = UsuarioPolicialForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioPolicialForm(instance=usuario)
    return render(request, 'policia1loja/agregar_editar_usuarios.html', {'form': form, 'usuario': usuario})

    #Eliminar Usuario
def eliminar_usuario(request, id):
    usuario = get_object_or_404(UsuarioPolicial, pk=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'policia1loja/eliminar_usuarios.html', {'usuario': usuario})

   #---------------------------------------------------------------------------------------------------------------Gestionar dependencias
def lista_dependencia(request):
    dependencias = Dependencia.objects.all()
    dependencias_filter = DependenciaFilter(request.GET, queryset=dependencias)
    return render(request, "policia1loja/lista_dependencias.html" , {"filter": dependencias_filter})
   
   
   #Agregar dependencia
def agregar_dependencia(request):
    if request.method == 'POST':
        form = Dependenciaform(request.POST)
        if form.is_valid():
           dependencia = form.save(commit=False)
           dependencia.save()
           messages.success(request, 'Dependencia agregada con éxito.')
           return redirect('lista_dependencias')  # Reemplaza con la URL a la que deseas redirigir
        else:
             for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field}: {error}")
    else:
        form = Dependenciaform()
    return render(request, 'policia1loja/agregar_dependencia.html', {'form': form})

    # Editar dependencia
def editar_dependencia(request, pk):
    dependencia = get_object_or_404(Dependencia, pk=pk)
    if request.method == 'POST':
        form = Dependenciaform(request.POST, instance=dependencia)
        if form.is_valid():
            form.save()
            return redirect('lista_dependencias')
    else:
        form = Dependenciaform(instance=dependencia)
    return render(request, 'policia1loja/editar_dependencia.html', {'form': form})

# Vista para eliminar una dependencia
#@require_POST  # Esta vista sólo debe aceptar solicitudes POST
def eliminar_dependencia(request, pk):
    dependencia = get_object_or_404(Dependencia, pk=pk)
    if request.method == 'POST':
        dependencia.delete()
        return redirect('lista_dependencias')
    return render(request, 'policia1loja/eliminar_dependencia.html', {'dependencia': dependencia})

   #-------------------------------------------------------------------------------------------------------------------------------Gestionar vehiculos
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "policia1loja/lista_vehiculos.html" , {"vehiculos": vehiculos})
   #Agregar vehiculo
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = Vehiculoform(request.POST)
        if form.is_valid():
           vehiculo = form.save(commit=False)
           vehiculo.save()
           messages.success(request, 'Vehículo agregado con éxito.')
           return redirect('lista_vehiculos')  # Reemplaza con la URL a la que deseas redirigir
        else:
             for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field}: {error}")
    else:
        form = Vehiculoform()
    return render(request, 'policia1loja/agregar_vehiculo.html', {'form': form})

    # Editar vehiculo
def editar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = Vehiculoform(request.POST, instance= vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = Vehiculoform(instance=vehiculo)
    return render(request, 'policia1loja/editar_vehiculo.html', {'form': form})

# Vista para eliminar un vehiculo
#@require_POST  # Esta vista sólo debe aceptar solicitudes POST
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('lista_vehiculos')
    return render(request, 'policia1loja/eliminar_vehiculo.html', {'vehiculo': vehiculo})


    
   #----------------------------------------------------------------------------------------------------------------------- Gestionar subcircuitos
def lista_subcircuito(request):
    subcircuitos = Subcircuito.objects.all()
    return render(request, "policia1loja/lista_subcircuitos.html" , {"subcircuitos": subcircuitos})

    #Agregar_Subcircuito
def agregar_subcircuito(request):
    if request.method == 'POST':
        form = SubcircuitoForm(request.POST)
        if form.is_valid():
           subcircuito = form.save(commit=False)
           dependencia_id = form.cleaned_data.get('dependencia').id  # Obtén el ID de la dependencia
           subcircuito.dependencia_id = dependencia_id  # Asigna el ID a la clave foránea
           subcircuito.save()
           messages.success(request, 'Subcircuito agregado con éxito.')
           return redirect('lista_subcircuitos')  # Reemplaza con la URL a la que deseas redirigir
        else:
             for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field}: {error}")
    else:
        form = SubcircuitoForm()
    return render(request, 'policia1loja/agregar_subcircuito.html', {'form': form})

    # Editar subcircuito
def editar_subcircuito(request, pk):
    subcircuito = get_object_or_404(Subcircuito, pk=pk)
    if request.method == 'POST':
        form = SubcircuitoForm(request.POST, instance=subcircuito)
        if form.is_valid():
            form.save()
            return redirect('lista_subcircuitos')
    else:
        form = SubcircuitoForm(instance=subcircuito)
    return render(request, 'policia1loja/editar_subcircuito.html', {'form': form})

# Vista para eliminar un subcircuito
#@require_POST  # Esta vista sólo debe aceptar solicitudes POST
def eliminar_subcircuito(request, pk):
    subcircuito = get_object_or_404(Subcircuito, pk=pk)
    if request.method == 'POST':
        subcircuito.delete()
        return redirect('lista_subcircuitos')
    return render(request, 'policia1loja/eliminar_subcircuito.html', {'subcircuito': subcircuito})


 # Asignación de usuario policial a un subcircuito

def asignar_subcircuitos(request, usuario_id):
    usuario = get_object_or_404(UsuarioPolicial, pk=usuario_id)
    if request.method == 'POST':
        form = AsignacionSubcircuitoForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')  # O la vista que desees
    else:
        form = AsignacionSubcircuitoForm(instance=usuario)

    return render(request, 'policia1loja/asignar_subcircuito.html', {'form': form, 'usuario': usuario})


def seleccionar_usuario_para_subcircuito(request):
    usuarios = UsuarioPolicial.objects.all()
    return render(request, 'policia1loja/seleccionar_usuario_para_subcircuito.html', {'usuarios': usuarios})


#Solicitud de Mantenimiento
def crear_solicitud_mantenimiento(request):
    if request.method == 'POST':
        form = SolicitudMantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes agregar la lógica para enviar el documento por correo electrónico o WhatsApp
            return redirect('ver_solicitudes_mantenimiento')
    else:
        form = SolicitudMantenimientoForm()
    return render(request, 'policia1loja/crear_solicitud_mantenimiento.html', {'form': form})


#Vista para solicitudes de mantenimiento

def ver_solicitudes_mantenimiento(request):
    solicitudes = SolicitudMantenimiento.objects.all().select_related('Usuario_Policial', 'Vehiculo')
    return render(request, 'policia1loja/ver_solicitudes_mantenimiento.html', {'solicitudes': solicitudes})


#Registro de mantenimiento preventivo
def registrar_mantenimiento_preventivo(request):
    if request.method == 'POST':
        form = MantenimientoPreventivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Generar orden de trabajo aquí si es necesario
            return redirect('lista_mantenimientos_preventivos')
    else:
        form = MantenimientoPreventivoForm()
    return render(request, 'policia1loja/registrar_mantenimiento_preventivo.html', {'form': form})

#Lista de mantenimientos registrados

def lista_mantenimientos_preventivos(request):
    mantenimientos = MantenimientoPreventivo.objects.all()
    return render(request, 'policia1loja/lista_mantenimientos_preventivos.html', {'mantenimientos': mantenimientos})


# descargar orden


def descargar_orden(request, mantenimiento_id):
    # Obtener el mantenimiento específico
    mantenimiento = MantenimientoPreventivo.objects.get(id=mantenimiento_id)

    # Crear una respuesta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="orden_mantenimiento_{}.pdf"'.format(mantenimiento_id)

    # Crear un PDF
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Orden de Mantenimiento Preventivo")  # Ejemplo básico
    # Aquí puedes agregar más detalles del mantenimiento

    p.showPage()
    p.save()
    return response

#Finalizar orden

def finalizar_mantenimiento(request, mantenimiento_id):
    # Obtener el objeto de mantenimiento
    mantenimiento = get_object_or_404(MantenimientoPreventivo, id=mantenimiento_id)

    # Marcar como finalizado
    mantenimiento.finalizado = True
    mantenimiento.save()

    # Redirigir a la lista de mantenimientos (o a otra página según necesidad)
    return redirect('lista_mantenimientos_preventivos')



#Orden de combustible
def index(request):
    return HttpResponse("Página de inicio")

@login_required
def list_orders(request):
    orders = OrdenCombustible.objects.all()
    return render(request, 'policia1loja/list_orders.html', {'orders': orders})

@login_required
@permission_required('policia1loja.add_ordencombustible', raise_exception=True)
def create_order(request):
    if request.method == 'POST':
        form = OrdenCombustibleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_orders')
    else:
        form = OrdenCombustibleForm()
    return render(request, 'policia1loja/create_order.html', {'form': form})

@login_required
@permission_required('policia1loja.change_ordencombustible', raise_exception=True)
def update_order(request, order_id):
    order = get_object_or_404(OrdenCombustible, id=order_id)
    if request.method == 'POST':
        form = OrdenCombustibleForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('list_orders')
    else:
        form = OrdenCombustibleForm(instance=order)
    return render(request, 'policia1loja/update_order.html', {'form': form})

@login_required
@permission_required('policia1loja.delete_ordencombustible', raise_exception=True)
def delete_order(request, order_id):
    order = get_object_or_404(OrdenCombustible, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('list_orders')
    return render(request, 'policia1loja/delete_order.html', {'order': order})



class OrdenCombustibleListCreate(generics.ListCreateAPIView):
    queryset = OrdenCombustible.objects.all()
    serializer_class = OrdenCombustibleSerializer

class OrdenCombustibleDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrdenCombustible.objects.all()
    serializer_class = OrdenCombustibleSerializer

    