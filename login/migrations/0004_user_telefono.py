# Generated by Django 5.0.3 on 2024-04-25 18:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_persona_mun_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)]),
        ),
    ]
