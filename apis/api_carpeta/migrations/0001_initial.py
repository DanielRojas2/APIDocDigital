# Generated by Django 5.1.4 on 2025-01-08 21:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloModalidadDespacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_despacho', models.CharField(choices=[('anticipado', 'anticipado'), ('abreviado', 'abreviado'), ('general', 'general')], max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Modalidad de despacho inválido', regex='^(anticipado|abreviado|general)')])),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Modalidad de Despacho',
                'verbose_name_plural': 'Modalidad de Despacho',
            },
        ),
        migrations.CreateModel(
            name='ModeloAduanaDespacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aduana_despacho', models.CharField(max_length=25, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Aduana Despacho',
                'verbose_name_plural': 'Aduana Despacho',
                'ordering': ['-creado'],
                'indexes': [models.Index(fields=['-creado'], name='api_carpeta_creado_85c4bb_idx')],
            },
        ),
        migrations.CreateModel(
            name='ModeloCanalApertura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_canal', models.CharField(choices=[('rojo', 'rojo'), ('amarillo', 'amarillo'), ('verde', 'verde')], max_length=8, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Canal de apertura inválido', regex='^(rojo|amarillo|verde)$')])),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Canal',
                'verbose_name_plural': 'Canal',
                'ordering': ['creado'],
                'indexes': [models.Index(fields=['-creado'], name='api_carpeta_creado_f3680f_idx')],
            },
        ),
        migrations.CreateModel(
            name='ModeloClasificacionCarpeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion_carpeta', models.CharField(choices=[('importación', 'Importación'), ('adminisión temporal', 'Admisión Temporal'), ('exportación definitiva', 'Exportación Definitiva'), ('ritex', 'Ritex')], max_length=22, unique=True, validators=[django.core.validators.RegexValidator(message='Clasificacion de carpeta inválida', regex='^(importación|adminisión temporal|exportación definitiva|ritex)$')])),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Clasificacion Carpeta',
                'verbose_name_plural': 'Clasificacion Carpetas',
                'ordering': ['creado'],
                'indexes': [models.Index(fields=['creado'], name='api_carpeta_creado_43a133_idx')],
            },
        ),
        migrations.CreateModel(
            name='ModeloImportador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_importador', models.CharField(max_length=50, unique=True)),
                ('nit_importador', models.CharField(max_length=20, unique=True)),
                ('tipo_importador', models.CharField(choices=[('unipersonal', 'Unipersonal'), ('empresa', 'Empresa')], max_length=11, validators=[django.core.validators.RegexValidator(message='Tipo de importador no válido', regex='^(unipersonal|empresa)$')])),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Importador',
                'verbose_name_plural': 'Importadores',
                'ordering': ['creado'],
                'indexes': [models.Index(fields=['creado'], name='api_carpeta_creado_3b6584_idx')],
            },
        ),
        migrations.CreateModel(
            name='ModeloMercaderia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mercaderia', models.CharField(max_length=75, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mercadería',
                'verbose_name_plural': 'Mercadería',
                'ordering': ['creado'],
                'indexes': [models.Index(fields=['creado'], name='api_carpeta_creado_53c16b_idx')],
            },
        ),
        migrations.CreateModel(
            name='ModeloPersonalAgencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_personal', models.CharField(max_length=25)),
                ('apellido_personal', models.CharField(max_length=25)),
                ('telefono_personal', models.CharField(blank=True, max_length=8, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal Agencia',
                'ordering': ['creado'],
                'indexes': [models.Index(fields=['creado'], name='api_carpeta_creado_332680_idx')],
                'constraints': [models.UniqueConstraint(fields=('nombre_personal', 'apellido_personal'), name='unique_nombre_apellido')],
            },
        ),
        migrations.CreateModel(
            name='ModeloTipoArchivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_archivo', models.CharField(max_length=55, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo Archivo',
                'verbose_name_plural': 'Tipo Archivos',
                'ordering': ['creado'],
                'indexes': [models.Index(fields=['creado'], name='api_carpeta_creado_a4e915_idx')],
            },
        ),
    ]
