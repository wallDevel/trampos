# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('cliente', '0002_cliente_usuario'),
        ('core', '0001_initial'),
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voto',
            name='to_restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resposta',
            name='cliente',
            field=models.ForeignKey(to='cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resposta',
            name='comentario',
            field=models.ForeignKey(to='core.Comentario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resposta',
            name='restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(to='cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='cliente',
            field=models.ForeignKey(to='cliente.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='restaurante',
            field=models.ForeignKey(to='restaurante.Restaurante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.OneToOneField(blank=True, to='core.Imagem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
