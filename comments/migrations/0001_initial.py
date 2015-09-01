# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_type', models.CharField(max_length=48, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('target_id', models.IntegerField(verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87ID')),
                ('content', models.TextField(max_length=1024, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('comment_from_id', models.IntegerField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85ID')),
                ('reply', models.ForeignKey(related_name='comment_reply', verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x9b\xae\xe6\xa0\x87', to='comments.Comment', null=True)),
            ],
        ),
    ]
