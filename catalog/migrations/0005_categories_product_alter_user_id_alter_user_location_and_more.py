# Generated by Django 4.0 on 2023-04-24 19:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Categories', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the category name (e.g. book)', max_length=80)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Product', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the product name (e.g. book)', max_length=80)),
                ('description', models.CharField(max_length=100)),
                ('Price', models.IntegerField(help_text='Enter the price')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Categories_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.categories')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for users', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(help_text='Enter a User location (e.g. Stanislawa Popowskiego 1, LODZ, Poland)', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='subCategories',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for subCategories', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the subcategory name (e.g. book)', max_length=80)),
                ('description', models.CharField(max_length=100)),
                ('Categories_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for review', primary_key=True, serialize=False)),
                ('Rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.CharField(help_text='comment', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.user')),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Seller_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.user'),
        ),
        migrations.AddField(
            model_name='product',
            name='subCategories_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.subcategories'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Order', primary_key=True, serialize=False)),
                ('Price', models.IntegerField(help_text='Enter the price')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.user')),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalog.product')),
            ],
        ),
    ]
