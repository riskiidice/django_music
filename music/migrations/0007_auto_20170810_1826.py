# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-10 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20170810_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=b''),
        ),
    ]