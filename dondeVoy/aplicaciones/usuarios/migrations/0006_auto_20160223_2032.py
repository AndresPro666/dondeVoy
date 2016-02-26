# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20160223_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizador',
            old_name='User',
            new_name='user',
        ),
    ]
