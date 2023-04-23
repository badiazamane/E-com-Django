from django.contrib import admin

# Register your models here.
from .models import User


# Register the admin class with the associated model
admin.site.register(User)
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(Language)
