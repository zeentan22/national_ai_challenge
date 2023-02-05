from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

def get_api_docs_view():
    schema_view = get_schema_view(
    openapi.Info(
        title="REST API Documentation",
        default_version='v1',
        description="Documentation for backend endpoints",
        terms_of_service="",
        contact=openapi.Contact(email="abc@abc.com"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    )

    return schema_view