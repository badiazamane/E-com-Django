# Generated by Django 4.0 on 2023-04-24 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_categories_product_alter_user_id_alter_user_location_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='subCategories',
            new_name='subCategory',
        ),
    ]
