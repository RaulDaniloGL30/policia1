# Generated by Django 5.0 on 2024-01-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policia1loja', '0008_rename_solicitud_id_solicitudmantenimiento_solicitud_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependencia',
            name='Codigo_distrito',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dependencia',
            name='Numero_circuito',
            field=models.CharField(default=123, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dependencia',
            name='Parroquia',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
