# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-24 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recite', '0002_auto_20170824_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voca', to='recite.Chapter', verbose_name='所属章节'),
        ),
    ]