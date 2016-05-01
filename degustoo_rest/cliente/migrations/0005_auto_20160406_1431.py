# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20160324_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagem',
            field=models.ImageField(verbose_name='Foto Perfil', null=True, upload_to='user_profile/', blank=True),
            preserve_default=True,
        ),
    ]
