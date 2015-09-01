# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AddField(
            model_name='comment',
            name='pud_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
