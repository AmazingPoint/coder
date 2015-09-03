# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_type', models.CharField(max_length=48, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('target_id', models.IntegerField(verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87ID')),
                ('content', models.TextField(max_length=1024, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('pud_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('from_user', models.ForeignKey(related_name='comment_user', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
                ('reply', models.ForeignKey(related_name='comment_reply', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x9b\xae\xe6\xa0\x87', to='comments.Comment', null=True)),
            ],
            options={
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
