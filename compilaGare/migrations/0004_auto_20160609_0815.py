# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-09 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilaGare', '0003_auto_20160608_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creteriogara',
            name='soglia',
            field=models.CharField(choices=[(None, ''), ('M', 'minore di 150.000'), ('C', 'compresi tra 150.000 e 1.000.000'), ('S', 'superiori a 1.000.000')], max_length=30),
        ),
        migrations.AlterField(
            model_name='creteriogara',
            name='tipo',
            field=models.CharField(choices=[(None, ''), ('L', 'Lavori'), ('S', 'Servizi'), ('F', 'Forniture')], max_length=30),
        ),
    ]
