from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from partners.views import ImportPartnerViewSet, PartnerViewSet, upload_file

router = routers.DefaultRouter()
router.register(
    r"api/import-partners", ImportPartnerViewSet, basename="import-partners"
)
router.register(r"api/partners", PartnerViewSet, basename="partners")

schema_view = get_schema_view(
    openapi.Info(
        title="Partners API",
        default_version="v1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("upload/", upload_file, name="upload_file"),
]
