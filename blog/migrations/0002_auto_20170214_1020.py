# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='nom',
            new_name='name',
        ),
    ]
