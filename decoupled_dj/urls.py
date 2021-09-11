from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("billing/", include("billing.urls", namespace="billing")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("auth/", include("login.urls", namespace="auth")),
]

if settings.DEBUG:
    urlpatterns = [
                      path("admin/", admin.site.urls),
                  ] + urlpatterns
if not settings.DEBUG:  # Protect Django Admin in production
    urlpatterns = [
                      path("77randomAdmin@33/", admin.site.urls),
                  ] + urlpatterns
