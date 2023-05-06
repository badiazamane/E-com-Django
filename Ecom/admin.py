from django.contrib import admin

# Register your models here.
from .models import User,Product,Order,Category,subCategory,Review


# Register the admin class with the associated model
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(subCategory)
admin.site.register(Review)


