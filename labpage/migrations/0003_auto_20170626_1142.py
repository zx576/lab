# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-26 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labpage', '0002_auto_20170626_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='pic/', verbose_name='配图'),
        ),
    ]
