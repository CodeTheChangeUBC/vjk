# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-09 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vjk', '0003_auto_20170708_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='province',
            field=models.CharField(blank=True, choices=[('YT', 'Yukon'), ('NS', 'Nova Scotia'), ('QC', 'Quebec'), ('MB', 'Manitoba'), ('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('NB', 'New Brunswick'), ('AB', 'Alberta'), ('SK', 'Saskatchewan'), ('NT', 'Northwest Territories'), ('BC', 'British Columbia')], max_length=20, null=True, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='student',
            name='province',
            field=models.CharField(blank=True, choices=[('YT', 'Yukon'), ('NS', 'Nova Scotia'), ('QC', 'Quebec'), ('MB', 'Manitoba'), ('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('NB', 'New Brunswick'), ('AB', 'Alberta'), ('SK', 'Saskatchewan'), ('NT', 'Northwest Territories'), ('BC', 'British Columbia')], max_length=20, null=True, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='student',
            name='reference_province',
            field=models.CharField(blank=True, choices=[('YT', 'Yukon'), ('NS', 'Nova Scotia'), ('QC', 'Quebec'), ('MB', 'Manitoba'), ('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('NB', 'New Brunswick'), ('AB', 'Alberta'), ('SK', 'Saskatchewan'), ('NT', 'Northwest Territories'), ('BC', 'British Columbia')], max_length=20, null=True, verbose_name='Ref. Province'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='province',
            field=models.CharField(blank=True, choices=[('YT', 'Yukon'), ('NS', 'Nova Scotia'), ('QC', 'Quebec'), ('MB', 'Manitoba'), ('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('NB', 'New Brunswick'), ('AB', 'Alberta'), ('SK', 'Saskatchewan'), ('NT', 'Northwest Territories'), ('BC', 'British Columbia')], max_length=20, null=True, verbose_name='Province'),
        ),
    ]