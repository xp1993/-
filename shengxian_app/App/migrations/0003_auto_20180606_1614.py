# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-06 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20180606_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='categoryid',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.FoodType', verbose_name='大类'),
        ),
    ]