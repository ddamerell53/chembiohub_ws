# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chembl_business_model', '0002_auto_20160224_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangocheatsheet',
            name='emailField',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='djangocheatsheet',
            name='ipAddressField',
            field=models.GenericIPAddressField(),
        ),
    ]
