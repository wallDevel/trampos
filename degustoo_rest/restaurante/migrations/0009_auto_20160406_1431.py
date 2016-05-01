# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0008_auto_20160326_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='imagem',
            field=models.ImageField(null=True, upload_to='menu_images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='imagem',
            field=models.ImageField(verbose_name='Logo Restaurante', null=True, upload_to='restaurant_profile', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='tipo',
            field=models.IntegerField(choices=[(0, 'Comum'), (1, 'Diamante')]),
            preserve_default=True,
        ),
    ]
