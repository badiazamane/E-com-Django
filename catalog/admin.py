from django.contrib import admin

# Register your models here.
from .models import Users


# Register the admin class with the associated model
admin.site.register(Users)
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(Language)
