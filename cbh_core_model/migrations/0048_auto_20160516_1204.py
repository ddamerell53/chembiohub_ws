# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-16 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbh_core_model', '0047_auto_20160516_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinnedcustomfield',
            name='attachment_field_mapped_to',
        ),
        migrations.RemoveField(
            model_name='pinnedcustomfield',
            name='standardised_alias',
        ),
    ]