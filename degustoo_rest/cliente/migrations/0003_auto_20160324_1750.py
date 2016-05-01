# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='carrinho',
        ),
        migrations.DeleteModel(
            name='Carrinho',
        ),
        migrations.AddField(
            model_name='cliente',
            name='foto_perfil',
            field=models.ImageField(null=True, upload_to=b'profiles/', blank=True),
            preserve_default=True,
        ),
    ]
