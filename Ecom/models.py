from django.db import models

# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid  # Required for unique  instances

from django.contrib.auth.models import User
from datetime import date
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=80, help_text="Enter the product name (e.g. Phone)"
    )
    description = models.TextField(max_length=1000)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Enter the price",
    )
    categories = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    subcategories = models.ForeignKey(
        "Subcategory", on_delete=models.CASCADE, related_name="products"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")

    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


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
