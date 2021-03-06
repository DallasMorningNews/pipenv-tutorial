# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-03 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('order', models.PositiveSmallIntegerField(default=10)),
            ],
            options={
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('order', models.PositiveSmallIntegerField(default=10)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.List')),
            ],
            options={
                'ordering': ['list__order', 'order', 'title'],
            },
        ),
    ]
