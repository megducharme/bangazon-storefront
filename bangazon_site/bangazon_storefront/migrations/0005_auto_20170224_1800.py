# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_storefront', '0004_merge_20170224_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttype',
            name='account_number',
            field=models.IntegerField(),
        ),
    ]