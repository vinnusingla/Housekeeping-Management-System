# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-19 15:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170219_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complainee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
