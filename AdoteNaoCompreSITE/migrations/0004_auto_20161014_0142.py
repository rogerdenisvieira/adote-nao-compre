# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 04:42
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('AdoteNaoCompreSITE', '0003_auto_20161013_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='IdRaca',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE,
                                    to='AdoteNaoCompreSITE.Breed'),
        ),
    ]
