# Generated by Django 5.0 on 2024-01-15 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policia1loja', '0006_rename_dependencia_id_usuariopolicial_dependencia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcircuito',
            name='Subcircuito_Id',
        ),
        migrations.RemoveField(
            model_name='subcircuito',
            name='dependencia_Id',
        ),
        migrations.AddField(
            model_name='subcircuito',
            name='dependencia',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='policia1loja.dependencia'),
            preserve_default=False,
        ),
    ]
