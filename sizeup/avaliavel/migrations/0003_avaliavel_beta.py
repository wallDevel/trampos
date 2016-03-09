# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_endereco_beta'),
        ('avaliavel', '0002_avaliavel_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliavel_Beta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=50, blank=True)),
                ('setor', models.CharField(max_length=100)),
                ('subsetor', models.CharField(max_length=100, blank=True)),
                ('endereco_beta', models.OneToOneField(to='core.Endereco_Beta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
