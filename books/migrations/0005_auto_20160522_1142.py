# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160522_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image_B',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='book_image_G',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='book_image_R',
            field=models.PositiveIntegerField(default=0),
        ),
    ]