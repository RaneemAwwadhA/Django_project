# Generated by Django 4.2.20 on 2025-04-04 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_categories_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='net',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AddIndex(
            model_name='categories',
            index=models.Index(fields=['name'], name='product_cat_name_d66187_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='product_pro_name_b60cd1_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['categories'], name='product_pro_categor_d822e0_idx'),
        ),
    ]
