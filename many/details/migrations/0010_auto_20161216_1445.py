# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-16 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0009_auto_20161216_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membership',
            options={'ordering': ('author',)},
        ),
    ]