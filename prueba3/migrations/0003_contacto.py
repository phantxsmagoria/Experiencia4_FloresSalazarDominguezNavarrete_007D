# Generated by Django 4.0.5 on 2022-06-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba3', '0002_alter_usuario_direccion_alter_usuario_apellido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('rut', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='RUT')),
                ('pnombre', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('telefono', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('dudas', models.CharField(max_length=500, verbose_name='Dudas y Consultas')),
            ],
        ),
    ]
