# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20160223_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizador',
            name='email',
            field=models.CharField(default=datetime.datetime(2016, 2, 23, 21, 28, 23, 856767, tzinfo=utc), max_length=80),
            preserve_default=False,
        ),
    ]
