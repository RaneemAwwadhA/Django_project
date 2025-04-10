# Generated by Django 4.2.20 on 2025-04-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_product_product_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='net',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='notes',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='total',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
