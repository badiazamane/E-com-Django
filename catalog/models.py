from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid  # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import RegexValidator

# !Users modele
class Users(models.Model):
    """Model representing a User."""
    name = models.CharField(
        max_length=100, help_text='Enter a User name (e.g. John Doe)')
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100, validators=[
        RegexValidator(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$',
                       'Password must be at least 8 characters long and contain at least one digit, one lowercase letter, and one uppercase letter.')
    ])
    location = models.CharField(
        max_length=100, help_text='Enter a User name (e.g. John Doe)')
    location = models.CharField(max_length=5, help_text='Enter a User name (e.g. John Doe)')
    
    phone = models.IntegerField(max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

