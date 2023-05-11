from django.urls import path
from Ecom.views import index, addAnnouncement, create_product, success_view
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("product_list/", addAnnouncement.as_view(), name="product_list"),
    path("products/create", create_product, name="create_product"),
    path("success/", success_view, name="success"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
