# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20170621_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='style',
            field=models.CharField(choices=[('contemporary', 'Contemporary'), ('modern', 'Modern')], default='contemporary', max_length=128),
        ),
    ]