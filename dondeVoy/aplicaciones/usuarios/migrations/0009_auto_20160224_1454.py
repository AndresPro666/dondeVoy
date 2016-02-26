# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20160224_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizador',
            name='imagenPerfil',
            field=models.ImageField(null=True, blank=True, upload_to='imagenesPerfil'),
        ),
    ]
