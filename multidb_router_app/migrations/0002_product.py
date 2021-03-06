# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-10 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multidb_router_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('sports', 'sports'), ('electronics', 'electronics'), ('fashion', 'fashion')], default=None, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multidb_router_app.DatabaseUser')),
            ],
        ),
    ]
