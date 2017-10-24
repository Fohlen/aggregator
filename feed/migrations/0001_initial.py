# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('url', models.URLField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('created', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
                ('content', models.TextField()),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Feed')),
            ],
            options={
                'get_latest_by': ['last_updated', 'created'],
            },
        ),
    ]