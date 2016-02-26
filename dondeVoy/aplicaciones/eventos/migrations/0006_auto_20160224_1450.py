# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20160224_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='imagenPortada',
            field=models.ImageField(blank=True, null=True, upload_to='/imagenesPortadas/'),
        ),
    ]
