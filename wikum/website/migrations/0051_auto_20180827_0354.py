# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-08-27 03:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_auto_20180826_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentrating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]