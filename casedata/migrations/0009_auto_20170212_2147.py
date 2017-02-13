# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casedata', '0008_case_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='point',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='casedata.Point'),
        ),
    ]