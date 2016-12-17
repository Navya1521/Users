# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-16 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_auto_20161216_0513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('my_order',)},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('my_order',)},
        ),
        migrations.AddField(
            model_name='author',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
