# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170830_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipstat',
            name='current_status',
            field=models.CharField(choices=[('Collecting', 'Collecting'), ('Processing', 'Processing'), ('In Transit', 'In Transit'), ('Delivering', 'Delivering'), ('Delivered', 'Delivered')], default='Collecting', max_length=11),
        ),
    ]