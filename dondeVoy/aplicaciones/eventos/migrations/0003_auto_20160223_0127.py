# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20160221_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='imagenPortada',
            field=models.ImageField(upload_to='media/imagenesPortadas/'),
        ),
    ]
