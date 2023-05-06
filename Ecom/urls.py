from django.urls import path
from Ecom.views import index

urlpatterns = [
    path('', index, name='index'), ]
