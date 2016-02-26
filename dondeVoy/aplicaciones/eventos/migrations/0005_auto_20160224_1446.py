# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20160224_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='imagenPortada',
            field=models.ImageField(blank=True, upload_to='/imagenesPortadas/'),
        ),
    ]
