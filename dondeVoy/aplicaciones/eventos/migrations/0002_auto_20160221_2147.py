# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20160221_2147'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombreCategoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombreEvento', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('estado', models.BooleanField()),
                ('calle', models.CharField(max_length=40)),
                ('altura', models.CharField(max_length=5)),
                ('imagenPortada', models.ImageField(upload_to='imagenesPortadas/')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombreLocalidad', models.CharField(max_length=50)),
                ('codigoPostal', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombrePais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombreProvincia', models.CharField(max_length=50)),
                ('pais', models.ForeignKey(to='eventos.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombreSubcategoria', models.CharField(max_length=50)),
                ('Categoria', models.ForeignKey(to='eventos.Categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=models.ForeignKey(to='eventos.Provincia'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='localidad',
            field=models.ForeignKey(to='eventos.Localidad'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='organizador',
            field=models.ForeignKey(to='usuarios.Organizador'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='subcategoria',
            field=models.ForeignKey(to='eventos.Subcategoria'),
        ),
    ]
