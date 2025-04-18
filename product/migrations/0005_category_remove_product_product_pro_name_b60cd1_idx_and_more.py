# Generated by Django 4.2.20 on 2025-04-04 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_categories_alter_product_net_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='product_pro_name_b60cd1_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='product_pro_categor_d822e0_idx',
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
