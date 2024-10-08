# Generated by Django 5.0.3 on 2024-08-20 05:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0003_alter_proveedor_prov_telefono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='Prov_telefono',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)], verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='sedeproveedor',
            name='Provs_telefono',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)], verbose_name='Telefono'),
        ),
    ]
