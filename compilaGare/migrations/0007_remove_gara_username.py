# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-15 09:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compilaGare', '0006_auto_20160615_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gara',
            name='username',
        ),
    ]
