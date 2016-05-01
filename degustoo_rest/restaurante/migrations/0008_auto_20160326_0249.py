# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0007_auto_20160324_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gerenciadorrestaurante',
            name='cpf',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gerenciadorrestaurante',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gerenciadorrestaurante',
            name='telefone',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
