# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-28 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='choice',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
