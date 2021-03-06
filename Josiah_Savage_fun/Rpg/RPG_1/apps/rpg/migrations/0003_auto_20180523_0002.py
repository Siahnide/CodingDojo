# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-23 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0002_auto_20180522_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char', to='rpg.Char')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='slot',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='equipment',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char', to='rpg.Item'),
        ),
    ]
