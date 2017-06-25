# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 01:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0007_auto_20170621_2300'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('discount', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('tax', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('total', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
            ],
        ),
    ]