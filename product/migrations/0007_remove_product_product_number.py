# Generated by Django 4.2.20 on 2025-04-05 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_product_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_number',
        ),
    ]
