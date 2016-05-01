# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0004_auto_20160324_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='imagem',
            field=models.ImageField(upload_to=b'restaurant_profile', null=True, verbose_name=b'Logo Restaurante', blank=True),
            preserve_default=True,
        ),
    ]
