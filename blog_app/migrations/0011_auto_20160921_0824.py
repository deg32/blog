# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_auto_20160921_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
