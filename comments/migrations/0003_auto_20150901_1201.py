# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0002_auto_20150901_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_from_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='from_user',
            field=models.ForeignKey(related_name='comment_user', default=1, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
