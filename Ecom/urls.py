from django.urls import path
from Ecom.views import index, addAnnouncement, create_product


urlpatterns = [
    path("", index, name="index"),
    path("product_list/", addAnnouncement.as_view(), name="product_list"),
    path("products/create", create_product, name="create_product"),
]
