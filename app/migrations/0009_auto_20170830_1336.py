# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170830_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusdetail',
            name='this_status',
            field=models.CharField(blank=True, choices=[('Collecting', 'Collecting'), ('Processing', 'Processing'), ('In Transit', 'In Transit'), ('Delivering', 'Delivering'), ('Delivered', 'Delivered')], max_length=11, null=True),
        ),
    ]
