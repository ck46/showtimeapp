# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190224_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='decodertype',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]