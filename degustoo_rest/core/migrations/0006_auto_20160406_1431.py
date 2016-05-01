# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160324_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='forma_pagamento',
            field=models.IntegerField(choices=[(0, 'Credit Card'), (1, 'Entrega')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='forma_retirada',
            field=models.IntegerField(choices=[(0, 'Pegar no caixa'), (1, 'Delivery')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.IntegerField(choices=[(0, 'Enviando'), (1, 'Preparando'), (2, 'Entregando'), (3, 'Estornado'), (4, 'Entregue')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voto',
            name='tipo',
            field=models.IntegerField(choices=[(0, '-'), (1, '+')]),
            preserve_default=True,
        ),
    ]
