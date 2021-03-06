# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-10 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0003_remove_areamodel_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToletCommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tolet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_home.ToLetModel')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
