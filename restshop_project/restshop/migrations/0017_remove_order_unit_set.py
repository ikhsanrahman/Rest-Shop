# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restshop', '0016_auto_20170830_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='unit_set',
        ),
    ]