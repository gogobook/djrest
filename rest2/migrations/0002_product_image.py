# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
