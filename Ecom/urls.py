from django.urls import path
from Ecom.views import index
from Ecom.views import addAnnouncement


urlpatterns = [
    path('', index, name='index'),
     path('product_list/', addAnnouncement.as_view(), name='product_list'),  ]
