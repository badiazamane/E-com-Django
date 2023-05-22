from django.urls import path, include
from Ecom.views import (
    index,
    addAnnouncement,
    create_product,
    my_products,
    success_view,
    register_user,
    login_user,
)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("product_list/", addAnnouncement.as_view(), name="product_list"),
    path("products/create", create_product, name="create_product"),
    path("my-products/", my_products, name="my_products"),
    path("success/", success_view, name="success"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
