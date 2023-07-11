# Generated by Django 4.0 on 2023-05-23 09:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Ecom', '0005_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Ecom.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Enter the price', max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Ecom.subcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='auth.user'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]