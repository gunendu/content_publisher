# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180828_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]