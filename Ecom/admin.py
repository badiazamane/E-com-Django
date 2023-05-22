from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# from .models import User
# from django.contrib.auth.models import User

# Register your models here.
from .models import Product, Order, Category, Subcategory, Review


# Register the admin class with the associated model
# admin.site.register(User)

# admin.site.register(User, UserAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Review)
