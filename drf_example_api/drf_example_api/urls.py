from django.contrib import admin
from django.urls import include, path

import rest_framework

from .users import user_router

urlpatterns = [
    path("", include(user_router.urls)),
    path("admin/", admin.site.urls),
    path("auth/", include(rest_framework.urls, namespace="rest_framework")),
]
