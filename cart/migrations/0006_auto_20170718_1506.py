# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cartitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='size',
            field=models.CharField(max_length=2),
        ),
    ]
