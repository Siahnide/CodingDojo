# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksauthors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='last_name',
        ),
    ]