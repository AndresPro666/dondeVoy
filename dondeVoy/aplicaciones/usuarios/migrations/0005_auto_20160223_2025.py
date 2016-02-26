# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_organizador_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizador',
            old_name='organizador',
            new_name='User',
        ),
    ]
