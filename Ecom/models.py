from django.db import models

# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid  # Required for unique  instances
from django.contrib.auth.models import User

from datetime import date
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# !Users modele


class User(models.Model):
    """Model representing a User."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, help_text="Enter a User name (e.g. John Doe)"
    )
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$",
                "Password must be at least 8 characters long and contain at least one digit, one lowercase letter, and one uppercase letter.",
            )
        ],
    )
    location = models.CharField(
        max_length=100,
        help_text="Enter a User location (e.g. Stanislawa Popowskiego 1, LODZ, Poland)",
    )
    phone = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Order(models.Model):
    """Model representing a product."""

    id = models.AutoField(primary_key=True)
    Price = models.IntegerField(help_text="Enter the price")
    buyer_ID = models.ForeignKey("User", on_delete=models.RESTRICT)
    product_ID = models.ForeignKey("Product", on_delete=models.RESTRICT)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Category(models.Model):
    """Model representing a product."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=80, help_text="Enter the category name (e.g. Fashion)"
    )
    description = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT, related_name="subcategories"
    )
    name = models.CharField(
        max_length=80, help_text="Enter the subcategory name (e.g. man clothes)"
    )
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=80, help_text="Enter the product name (e.g. Phone)"
    )
    description = models.TextField(max_length=1000)
    price = models.IntegerField(help_text="Enter the price")
    categories = models.ForeignKey(
        "Category", on_delete=models.RESTRICT, related_name="products"
    )
    subcategories = models.ForeignKey(
        "Subcategory", on_delete=models.RESTRICT, related_name="products"
    )
    user = models.ForeignKey("User", on_delete=models.RESTRICT, related_name="products")

    image = models.ImageField(upload_to="product_images/", null=True, blank=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Review(models.Model):
    """Model representing a product."""

    id = models.AutoField(primary_key=True)
    Rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.CharField(max_length=200, help_text="comment")
    created_date = models.DateTimeField(default=timezone.now)
    buyer_ID = models.ForeignKey("User", on_delete=models.RESTRICT)
    product_ID = models.ForeignKey("Product", on_delete=models.RESTRICT)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


# class Subcategory(models.Model):
#     """Model representing a Subcategory."""

#     id = models.AutoField(primary_key=True)
#     name = models.CharField(
#         max_length=80, help_text="Enter the subcategory name (e.g. man clothes)"
#     )
#     description = models.CharField(max_length=100)
#     Categories_ID = models.ForeignKey("Category", on_delete=models.RESTRICT)

#     def __str__(self):
#         """String for representing the Model object."""
#         return self.name


# class Product(models.Model):
#     """Model representing a product."""

#     id = models.AutoField(primary_key=True)
#     name = models.CharField(
#         max_length=80, help_text="Enter the product name (e.g. Phone)"
#     )
#     description = models.CharField(max_length=100)
#     Price = models.IntegerField(help_text="Enter the price")
#     # Seller_ID = models.ForeignKey("User", on_delete=models.RESTRICT)
#     Categories_ID = models.ForeignKey("Category", on_delete=models.RESTRICT)
#     Subcategories = models.ForeignKey("Subcategory", on_delete=models.RESTRICT)
#     created_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         """String for representing the Model object."""
#         return self.name
