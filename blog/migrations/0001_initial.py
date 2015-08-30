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
            name='Articel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('is_pub', models.BooleanField(default=False)),
                ('author', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='ITMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=48, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': '\u6280\u672f\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='articel',
            name='meta',
            field=models.ManyToManyField(related_name='articel_meta', verbose_name=b'\xe6\x8a\x80\xe6\x9c\xaf\xe6\xa0\x87\xe7\xad\xbe', to='blog.ITMeta'),
        ),
    ]
