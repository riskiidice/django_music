# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-10 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20170810_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
