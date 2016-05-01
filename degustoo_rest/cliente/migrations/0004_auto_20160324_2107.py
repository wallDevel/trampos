# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20160324_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='foto_perfil',
        ),
        migrations.AddField(
            model_name='cliente',
            name='imagem',
            field=models.ImageField(upload_to=b'user_profile/', null=True, verbose_name=b'Foto Perfil', blank=True),
            preserve_default=True,
        ),
    ]
