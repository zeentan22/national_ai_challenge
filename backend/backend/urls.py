from django.contrib import admin
from django.urls import path, include
from .yasg_configs import get_api_docs_view

schema_view = get_api_docs_view()

urlpatterns = [
    # documentation for API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # app urls
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/sentiment/", include("sentiment.urls")),
]
