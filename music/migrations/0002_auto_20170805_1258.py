# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-05 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_type',
            new_name='song_title',
        ),
    ]
