# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20160221_2147'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0002_auto_20160221_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('fecha', models.DateTimeField()),
                ('comentario', models.CharField(max_length=500)),
                ('evento', models.ForeignKey(to='eventos.Eventos')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
