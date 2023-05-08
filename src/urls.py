from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from partners.views import ImportPartnerViewSet, PartnerViewSet, upload_file

router = routers.DefaultRouter()
router.register(
    r"api/import-partners", ImportPartnerViewSet, basename="import-partners"
)
router.register(r"api/partners", PartnerViewSet, basename="partners")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("upload/", upload_file, name="upload_file"),
]
