# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbh_chembl_model_extension', '0037_cbhcompoundmultiplebatch_batch_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cbhcompoundmultiplebatch',
            name='saved',
        ),
        migrations.AddField(
            model_name='cbhcompoundmultiplebatch',
            name='task_id_for_save',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
