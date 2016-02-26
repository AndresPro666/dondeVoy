# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20160223_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizador',
            name='imagenPerfil',
            field=models.ImageField(upload_to='imagenesPerfil'),
        ),
    ]
