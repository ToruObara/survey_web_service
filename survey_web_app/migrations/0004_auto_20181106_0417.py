# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('survey_web_app', '0003_auto_20181106_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='creation',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
