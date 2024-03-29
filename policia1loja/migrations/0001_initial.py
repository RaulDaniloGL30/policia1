# Generated by Django 5.0 on 2023-12-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioPolicial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('tipo_sangre', models.CharField(max_length=3)),
                ('ciudad_nacimiento', models.CharField(max_length=100)),
                ('telefono_celular', models.CharField(max_length=20)),
                ('rango_grado', models.CharField(max_length=50)),
                ('dependencia_id', models.CharField(max_length=40)),
                ('Usuario', models.CharField(max_length=30)),
                ('Contraseña', models.CharField(max_length=30)),
            ],
        ),
    ]
