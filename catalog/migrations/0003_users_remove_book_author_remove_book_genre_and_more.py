# Generated by Django 4.0 on 2023-04-17 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_book_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a User name (e.g. John Doe)', max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', 'Password must be at least 8 characters long and contain at least one digit, one lowercase letter, and one uppercase letter.')])),
                ('location', models.CharField(help_text='Enter a User name (e.g. John Doe)', max_length=5)),
                ('phone', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='borrower',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]