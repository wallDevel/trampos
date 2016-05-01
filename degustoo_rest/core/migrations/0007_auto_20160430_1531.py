# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0009_auto_20160406_1431'),
        ('core', '0006_auto_20160406_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_pedido',
            name='itens',
            field=models.ManyToManyField(to='restaurante.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item_pedido',
            name='opcao',
            field=models.ForeignKey(default=datetime.datetime(2016, 4, 30, 18, 30, 59, 681855, tzinfo=utc), to='restaurante.Opcao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_pedido',
            name='pedido',
            field=models.ForeignKey(default=1, to='core.Pedido'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_pedido',
            name='preco',
            field=models.DecimalField(max_digits=6, default=0, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item_pedido',
            name='subcardapios',
            field=models.ForeignKey(default=1, to='restaurante.Subcardapio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='endereco',
            field=models.ForeignKey(default=1, to='core.Endereco'),
            preserve_default=False,
        ),
    ]
