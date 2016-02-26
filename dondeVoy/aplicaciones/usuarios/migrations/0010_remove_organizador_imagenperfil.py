# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20160224_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizador',
            name='imagenPerfil',
        ),
    ]
