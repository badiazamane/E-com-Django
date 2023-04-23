from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid  # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import RegexValidator

# !Users modele

class User(models.Model):
    """Model representing a User."""
    name = models.CharField(
        max_length=100, help_text='Enter a User name (e.g. John Doe)')
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100, validators=[
        RegexValidator(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$',
                       'Password must be at least 8 characters long and contain at least one digit, one lowercase letter, and one uppercase letter.')
    ])
    location = models.CharField(
        max_length=100, help_text='Enter a User location (e.g. Stanislawa Popowskiego 1, LODZ, Poland)')
    zipcode = models.CharField(max_length=6, help_text='Enter a User location zipcode (e.g. 90-328)')
    
    phone = models.IntegerField(max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(
        max_length=80, help_text='Enter the product name (e.g. book)')
    description = models.CharField(max_length=100)
    Price = models.IntegerField(help_text='Enter the price')


    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Order(models.Model):
    """Model representing a product."""
    Price = models.IntegerField(help_text='Enter the price')
    #  ! order_date 
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Categories(models.Model):
    """Model representing a product."""
    name = models.CharField(
        max_length=80, help_text='Enter the category name (e.g. book)')
    description = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class subCategories(models.Model):
    """Model representing a product."""
    name = models.CharField(
        max_length=80, help_text='Enter the subcategory name (e.g. book)')
    description = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name