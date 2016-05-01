# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('imagem', models.OneToOneField(blank=True, to='core.Imagem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.DecimalField(default=0, max_digits=4, decimal_places=2)),
                ('cardapio', models.ForeignKey(to='restaurante.Cardapio', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rotulo', models.CharField(max_length=50)),
                ('cardapio', models.ForeignKey(to='restaurante.Cardapio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=50)),
                ('endereco', models.OneToOneField(to='core.Endereco')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('cardapio', models.ForeignKey(to='restaurante.Cardapio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='opcao',
            field=models.ForeignKey(to='restaurante.Opcao', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='sub_cardapio',
            field=models.ForeignKey(to='restaurante.Subcardapio', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cardapio',
            name='restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
    ]
