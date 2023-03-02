"""Yummo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Yuumo API",
      default_version='v1',
      description="Here lies all the available endpoints for Yummo",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include("RestaurantAPI.urls")),
    path('api/', include("YummoGroupAPI.urls")),
]

# For media files
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        

"""Djoser package's authentication endpoints (for reference)
    auth/users/
    auth/users/me/
    auth/users/confirm/
    auth/users/resend_activation/
    auth/users/set_password/
    auth/users/reset_password/
    auth/users/rest_password_confirm/
    auth/users/set_username/
    auth/users/reset_username/
    auth/users/reset_username_confirm/
    auth/token/login/
    auth/token/logout/
"""
