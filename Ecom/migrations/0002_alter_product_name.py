# Generated by Django 4.0 on 2023-05-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Enter the product name (e.g. Phone)', max_length=80),
        ),
    ]
