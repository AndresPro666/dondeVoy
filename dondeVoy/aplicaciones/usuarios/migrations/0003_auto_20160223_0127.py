# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20160221_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizador',
            name='imagenPerfil',
            field=models.ImageField(upload_to='media/imagenesPerfil/'),
        ),
    ]
