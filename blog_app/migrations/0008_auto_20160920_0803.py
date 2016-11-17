# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_user_subscribed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subscribe_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog_app.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]