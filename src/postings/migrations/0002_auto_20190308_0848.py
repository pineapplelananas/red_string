# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-08 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='time',
            field=models.IntegerField(),
        ),
    ]
