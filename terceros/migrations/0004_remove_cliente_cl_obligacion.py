# Generated by Django 5.0.3 on 2024-06-18 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0003_cliente_usr_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Cl_obligacion',
        ),
    ]
