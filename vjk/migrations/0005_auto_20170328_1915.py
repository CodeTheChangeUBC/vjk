# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 02:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vjk', '0004_auto_20170328_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donors',
            name='primary_contact',
        ),
        migrations.RemoveField(
            model_name='donors',
            name='secondary_contact',
        ),
    ]