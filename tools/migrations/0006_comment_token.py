# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20170718_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='token',
            field=models.CharField(default='index', max_length=50, verbose_name='页面标记'),
        ),
    ]
