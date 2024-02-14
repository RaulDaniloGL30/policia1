from django.db import models
from django.utils import timezone

class UsuarioPolicial(models.Model):
    identificacion = models.CharField(max_length=20)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    tipo_sangre = models.CharField(max_length=3)
    ciudad_nacimiento = models.CharField(max_length=100)
    telefono_celular = models.CharField(max_length=20)
    rango_grado = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=60)
    dependencia = models.ForeignKey( "Dependencia", on_delete=models.CASCADE)
    subcircuito = models.ForeignKey('Subcircuito', on_delete=models.SET_NULL, null=True, blank=True)
   
class Dependencia (models.Model):
    Provincia = models.CharField(max_length=30)
    Numero_distrito = models.CharField(max_length=30)
    Parroquia = models.CharField(max_length=30)
    Codigo_distrito = models.CharField(max_length=30)
    Nombre_distrito = models.CharField(max_length=30)
    Numero_circuito = models.CharField(max_length=15)
    Nombre_circuito = models.CharField(max_length=30)
    Codigo_circuito = models.CharField(max_length=30)
    Numero_subcircuito = models.CharField(max_length=30)
    Codigo_subcircuito = models.CharField(max_length=30)
    Nombre_subcircuito = models.CharField(max_length=30)
    def __str__(self):
        return self.Provincia  # o cualquier otro campo representativo
    
    
class Subcircuito (models.Model):
    Codigo_subcircuito = models.CharField(max_length=30)
    Nombre_subcircuito = models.CharField(max_length=30)
    dependencia = models.ForeignKey( "Dependencia", on_delete=models.CASCADE) # (FK a la tabla Dependencia)
    def __str__(self):
        return self.Nombre_subcircuito
     
class AsignacionSubcircuito (models.Model):
    Subcircuito = models.ForeignKey( "Subcircuito", on_delete=models.CASCADE) # (FK a la tabla Subcircuito)
    Usuario_Policial = models.ForeignKey( "UsuarioPolicial", on_delete=models.CASCADE)
class Vehiculo (models.Model):
    Tipo_Vehiculo = models.CharField(max_length=20)
    Placa = models.CharField(max_length=20)
    Chasis = models.CharField(max_length=20)
    Marca = models.CharField(max_length=20)
    Modelo = models.CharField(max_length=20)
    Motor = models.CharField(max_length=20)
    Kilometraje = models.IntegerField()
    Cilindraje = models.IntegerField()
    Capacidad_Carga = models.IntegerField()
    Capacidad_Pasajeros = models.IntegerField()
    def __str__(self):
        return self.Placa

class AsignacionVehiculoSubcircuito (models.Model):
    Vehiculo = models.ForeignKey( "Vehiculo", on_delete=models.CASCADE) #(FK de la tabla vehiculo)
    Subcircuito = models.ForeignKey( "Subcircuito", on_delete=models.CASCADE)# (FK a la tabla subcircuito)

class MantenimientoPreventivo(models.Model):
    TIPOS_MANTENIMIENTO = [
        ('M1', 'Mantenimiento 1'),
        ('M2', 'Mantenimiento 2'),
        ('M3', 'Mantenimiento 3'),
    ]
    
    Vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    Usuario_Policial = models.ForeignKey('UsuarioPolicial', on_delete=models.CASCADE)
    fecha_hora_ingreso = models.DateTimeField(default=timezone.now)
    kilometraje_actual = models.IntegerField()
    tipo_mantenimiento = models.CharField(max_length=2, choices=TIPOS_MANTENIMIENTO)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_parte_policial = models.ImageField(upload_to='partes_policiales/')

    def __str__(self):
        return f"{self.Vehiculo.Placa} - {self.get_tipo_mantenimiento_display()}"
    
    finalizado = models.BooleanField(default=False)
    

     

class SolicitudMantenimiento(models.Model):
    Usuario_Policial = models.ForeignKey('UsuarioPolicial', on_delete=models.CASCADE)
    Vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(default=timezone.now)
    kilometraje_actual = models.IntegerField()
    observaciones = models.TextField()

    def __str__(self):
        return f"Solicitud de {self.Usuario_Policial.nombres} para {self.Vehiculo.placa}"

class Orden_Trabajo (models.Model):
    Orden_Id= models.CharField(max_length=30)# PK
    Mantenimiento_Id = models.CharField(max_length=30) # FK

class Modulo (models.Model):
    Modulo_Id = models.CharField (max_length=40) # PK
    Nombre_Modulo = models.CharField (max_length=40)

class Rol (models.Model):
    Rol_Id = models.CharField (max_length=40) # PK
    Nombre_Rol = models.CharField (max_length=40)
    Descripcion_Rol = models.CharField (max_length=100)

class AsignacionRol (models.Model):
    Asignacion_Rol_Id = models.CharField ( max_length=50) # PK
    Usuario_Policial_Id = models.CharField(max_length=40)# FK tabla UsuarioPolicial
    Asignacion_Rol_Id = models.CharField (max_length=40)# Fk tabla Rol

class OrdenCombustible (models.Model):
    vehiculo = models.ForeignKey(Vehiculo , on_delete=models.CASCADE)
    Fecha = models.DateField(default=timezone.now)
    Cantidad = models.DecimalField(max_digits=6, decimal_places=2)
    Tipo_Combustible = models.CharField(max_length=30)
    Esta_Aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"Orden de Combustible para {self.vehiculo} on {self.Fecha.strftime('%Y-%m-%d')}"


