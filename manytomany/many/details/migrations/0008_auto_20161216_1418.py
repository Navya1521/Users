# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-16 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_auto_20161216_1413'),
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
    ]