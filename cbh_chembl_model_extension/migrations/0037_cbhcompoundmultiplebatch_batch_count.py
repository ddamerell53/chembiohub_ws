# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-24 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbh_chembl_model_extension', '0036_cbhcompoundmultiplebatch_uploaded_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbhcompoundmultiplebatch',
            name='batch_count',
            field=models.IntegerField(default=0),
        ),
    ]