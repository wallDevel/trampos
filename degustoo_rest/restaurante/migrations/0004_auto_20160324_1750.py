# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0003_item_ingredientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='imagem',
            field=models.ImageField(null=True, upload_to=b'menu_images/', blank=True),
            preserve_default=True,
        ),
    ]
