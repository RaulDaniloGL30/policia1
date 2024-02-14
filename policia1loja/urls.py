from django.urls import path
from . import views
from .views import OrdenCombustibleListCreate, OrdenCombustibleDetailUpdateDelete
#urlpatterns = [
   # path('', views.lista_usuarios, name='lista_usuarios'),]
  


urlpatterns = [
    path('orden/', views.list_orders, name='list_orders'),
    path('', views.index, name='index'),
    path('orden/create/', views.create_order, name='create_order'),
    path('orden/update/<int:order_id>/', views.update_order, name='update_order'),
    path('orden/delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('api/ordenes/', OrdenCombustibleListCreate.as_view(), name='ordenes-list-create'),
    path('api/ordenes/<int:pk>/', OrdenCombustibleDetailUpdateDelete.as_view(), name='ordenes-detail-update-delete'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name= "editar_usuario"),
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name= "eliminar_usuario"),
    path('inicio/', views.inicio, name='inicio'),
    path('dependencias/', views.lista_dependencia, name='lista_dependencias'),
    path('subcircuitos/', views.lista_subcircuito, name='lista_subcircuitos'),
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('subcircuitos/agregar/', views.agregar_subcircuito, name='agregar_subcircuito'),
    path('vehiculos/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('dependencias/agregar/', views.agregar_dependencia, name='agregar_dependencia'),
    path('subcircuitos/editar/<int:pk>/', views.editar_subcircuito, name='editar_subcircuito'),
    path('dependencias/editar/<int:pk>/', views.editar_dependencia, name='editar_dependencia'),
    path('vehiculos/editar/<int:pk>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('subcircuitos/eliminar/<int:pk>/', views.eliminar_subcircuito, name='eliminar_subcircuito'),
    path('dependencias/eliminar/<int:pk>/', views.eliminar_dependencia, name='eliminar_dependencia'),
    path('vehiculos/eliminar/<int:vehiculo_id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('asignar_subcircuitos/<int:usuario_id>/', views.asignar_subcircuitos, name='asignar_subcircuitos'),
    path('reportes/generar/', views.generar_reporte, name='generar_reporte'),
    path('seleccionar_usuario_para_subcircuito/', views.seleccionar_usuario_para_subcircuito, name='seleccionar_usuario_para_subcircuito'),
    path('solicitud-mantenimiento/crear/', views.crear_solicitud_mantenimiento, name='crear_solicitud_mantenimiento'),
    path('solicitudes-mantenimiento/ver/', views.ver_solicitudes_mantenimiento, name='ver_solicitudes_mantenimiento'),
    path('mantenimiento-preventivo/registrar/',views.registrar_mantenimiento_preventivo, name='registrar_mantenimiento_preventivo'),
    path('mantenimiento-preventivo/lista/',views.lista_mantenimientos_preventivos, name='lista_mantenimientos_preventivos'),
    path('mantenimiento-preventivo/descargar/<int:mantenimiento_id>/', views.descargar_orden, name='descargar_orden'),
    path('mantenimiento-preventivo/finalizar/<int:mantenimiento_id>/', views.finalizar_mantenimiento, name='finalizar_mantenimiento'),
]





  
