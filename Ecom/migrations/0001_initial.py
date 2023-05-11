# Generated by Django 4.0 on 2023-05-10 11:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the category name (e.g. Fashion)', max_length=80)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the product name (e.g. Phone)', max_length=80)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField(help_text='Enter the price')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='Ecom.category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter a User name (e.g. John Doe)', max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', 'Password must be at least 8 characters long and contain at least one digit, one lowercase letter, and one uppercase letter.')])),
                ('location', models.CharField(help_text='Enter a User location (e.g. Stanislawa Popowskiego 1, LODZ, Poland)', max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the subcategory name (e.g. man clothes)', max_length=80)),
                ('description', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='subcategories', to='Ecom.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.CharField(help_text='comment', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Ecom.user')),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Ecom.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='Ecom.subcategory'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Price', models.IntegerField(help_text='Enter the price')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Ecom.user')),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Ecom.product')),
            ],
        ),
    ]
