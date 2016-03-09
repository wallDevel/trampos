# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='imagem',
            field=models.OneToOneField(null=True, blank=True, to='core.Imagem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='cardapio',
            field=models.ForeignKey(blank=True, to='restaurante.Cardapio', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='opcao',
            field=models.ForeignKey(blank=True, to='restaurante.Opcao', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='sub_cardapio',
            field=models.ForeignKey(blank=True, to='restaurante.Subcardapio', null=True),
            preserve_default=True,
        ),
    ]
