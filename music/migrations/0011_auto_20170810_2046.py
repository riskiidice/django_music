# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-10 13:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_auto_20170810_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default=datetime.datetime(2017, 8, 10, 13, 46, 53, 130330, tzinfo=utc), upload_to=b'album/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
