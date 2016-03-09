# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0002_auto_20160302_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ingredientes',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
