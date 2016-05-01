# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0005_restaurante_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='GerenciadorRestaurante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('telefone', models.CharField(unique=True, max_length=50)),
                ('nome_completo', models.CharField(max_length=100)),
                ('cpf', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='gerenciador',
            field=models.ForeignKey(default=0, to='restaurante.GerenciadorRestaurante'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurante',
            name='tipo',
            field=models.IntegerField(default=1, choices=[(0, b'Comum'), (1, b'Diamante')]),
            preserve_default=False,
        ),
    ]
