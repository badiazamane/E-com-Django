from django.urls import path, include
from Ecom.views import (
    index,
    addAnnouncement,
    create_product,
    my_products,
    my_history,
    success_view,
    register_user,
    login_user,
    purchase_product,
    product_detail_view,
)


from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("product_list/", addAnnouncement.as_view(), name="product_list"),
    path("products/create", create_product, name="create_product"),
    path("success/", success_view, name="success"),
    path("my_products/", my_products, name="my_products"),
    path("my_history/", my_history, name="my_history"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("product/<int:product_id>/", product_detail_view, name="product_detail"),
    path(
        "purchase_product/<int:product_id>/",
        purchase_product,
        name="purchase_product",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
