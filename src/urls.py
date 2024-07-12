from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from home.api import api_router
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from search import views as search_views

from django.urls import path
from contacts.views import (
    ContactsFormSubmissionAPI,
    CalculateFormPricePageAPIView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Wagtail Dev cons API",
        default_version="v2",
        description="This is an api for backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        "redoc/",
        schema_view.with_ui(
            "redoc",
            cache_timeout=0
        ),
        name="schema-redoc"
    ),
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("api/v2/", api_router.urls),
    path(
        "api/v2/contacts/",
        ContactsFormSubmissionAPI.as_view(),
        name="contacts_submission_api",
    ),
    path(
        "api/v2/calculate-price/",
        CalculateFormPricePageAPIView.as_view(),
        name="calculate_price_api",
    )
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    path("", include(wagtail_urls)),
]
