# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import bitpoll.base.validators


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_auto_20170328_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='timezone_name',
            field=models.CharField(default='Europe/Berlin', max_length=40, validators=[ bitpoll.base.validators.validate_timezone ]),
        ),
    ]
