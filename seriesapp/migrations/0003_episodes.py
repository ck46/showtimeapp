# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-27 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seriesapp', '0002_auto_20190225_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publishedDate', models.IntegerField(blank=True, null=True)),
                ('episodesImages', models.FileField(null=True, upload_to=b'Series/SeriesImage/')),
                ('episodesVideo', models.FileField(null=True, upload_to=b'Series/SerieVideo/')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seriesapp.Series')),
            ],
        ),
    ]
