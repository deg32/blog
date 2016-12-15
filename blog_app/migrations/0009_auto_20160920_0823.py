# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 08:23
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('blog_app', '0008_auto_20160920_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_ptr',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='subscribe_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
