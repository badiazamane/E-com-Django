from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("Ecom/", include("Ecom.urls")),
    path("", RedirectView.as_view(url="Ecom/")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
