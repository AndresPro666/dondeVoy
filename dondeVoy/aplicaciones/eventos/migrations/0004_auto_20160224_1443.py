# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20160223_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='imagenPortada',
            field=models.ImageField(upload_to='/imagenesPortadas/'),
        ),
    ]
