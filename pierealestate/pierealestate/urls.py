from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("listings/", include("listings.urls")),
    path("realtors/", include("realtors.urls")),
    path("contacts/", include("contacts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
