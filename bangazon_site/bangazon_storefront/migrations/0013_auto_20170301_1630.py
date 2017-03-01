# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_storefront', '0012_auto_20170301_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField(default=1)),
                ('product_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bangazon_storefront.ProductTypes')),
                ('seller', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bangazon_storefront.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='productsmodel',
            name='categoryId',
        ),
        migrations.RemoveField(
            model_name='productsmodel',
            name='seller_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='bangazon_storefront.Product_On_Order', to='bangazon_storefront.Product'),
        ),
        migrations.AlterField(
            model_name='product_on_order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_on_order', to='bangazon_storefront.Product'),
        ),
        migrations.DeleteModel(
            name='ProductsModel',
        ),
    ]
