# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0004_auto_20160324_1750'),
        ('core', '0003_auto_20160301_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='avatar',
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RenameField(
            model_name='voto',
            old_name='from_cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='voto',
            old_name='to_restaurante',
            new_name='restaurante',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='send_date',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='restaurante',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='send_date',
        ),
        migrations.AddField(
            model_name='comentario',
            name='data_envio',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 24, 20, 49, 11, 882000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='data_envio',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 24, 20, 49, 19, 347000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='forma_pagamento',
            field=models.IntegerField(default=0, choices=[(0, b'Credit Card'), (1, b'Entrega')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='forma_retirada',
            field=models.IntegerField(default=0, choices=[(0, b'Pegar no caixa'), (1, b'Delivery')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='observacao',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Enviando'), (1, b'Preparando'), (2, b'Entregando'), (3, b'Estornado'), (4, b'Entregue')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='troco_para',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=6, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resposta',
            name='data_envio',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 24, 20, 50, 25, 827000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
