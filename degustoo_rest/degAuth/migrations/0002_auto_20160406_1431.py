# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('degAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nivel',
            field=models.IntegerField(choices=[(0, 'ADMIN'), (1, 'CLIENTE'), (2, 'RESTAURANTE')]),
            preserve_default=True,
        ),
    ]
