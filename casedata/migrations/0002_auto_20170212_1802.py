# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('casedata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='opened',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='case',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
