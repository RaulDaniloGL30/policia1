from django.core.management.base import BaseCommand
from policia1loja.models import UsuarioPolicial
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Puebla la base de datos con usuarios policiales'

    def handle(self, *args, **options):



        #UsuarioPolicial.objects.bulk_create([
            # UsuarioPolicial(nombres='Kendry Alonso',apellidos= "Paez Sanchez", fecha_nacimiento= "1993-10-28", tipo_sangre= "A+", ciudad_nacimiento= "Caluma", telefono_celular= "073763653617", rango_grado='Capitan', dependencia_id ='Loja', Usuario= "00001", Contraseña= "00000"),
             # UsuarioPolicial(nombres='Miller Andrés',apellidos= "Salazar Montero", fecha_nacimiento= "1990-11-30", tipo_sangre= "A+", ciudad_nacimiento= "Caluma", telefono_celular= "073763653617", rango_grado='Sargento', dependencia_id ='Loja', Usuario= "00002", Contraseña= "00000"),
            
#])
         
        self.stdout.write(self.style.SUCCESS('Usuarios policiales creados exitosamente.'))
