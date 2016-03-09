# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_usuario_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco_Beta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=50, blank=True)),
                ('municipio', models.CharField(max_length=50, blank=True)),
                ('bairro', models.CharField(max_length=50, blank=True)),
                ('rua', models.CharField(max_length=50, blank=True)),
                ('numero', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
