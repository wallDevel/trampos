# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0006_auto_20160324_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='gerenciador',
            field=models.OneToOneField(to='restaurante.GerenciadorRestaurante'),
            preserve_default=True,
        ),
    ]
