# Generated by Django 5.0.3 on 2024-06-22 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0006_rename_per_nombre_cliente_cl_nombre'),
        ('transacciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='Prov_codigo',
        ),
        migrations.AddField(
            model_name='compra',
            name='Cl_codigo',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='terceros.cliente', verbose_name='Cliente'),
            preserve_default=False,
        ),
    ]
