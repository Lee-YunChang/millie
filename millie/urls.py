"""millie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.http import JsonResponse
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger 스키마 설정
schema_view = get_schema_view(
   openapi.Info(
      title="Millie API",
      default_version='v1',
      description="Millie 프로젝트 API 문서",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@millie.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('services.product.urls')),
    path('', include('services.coupon.urls')),
    path('', include('services.category.urls')),


    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
def not_found(request, exception, *args, **kwargs):  # pylint: disable=unused-argument
    # The body should be empty to be consistent with alb's fixed response
    return JsonResponse(data={}, status=HTTP_404_NOT_FOUND)


def internal_server_error(request, *args, **kwargs):  # pylint: disable=unused-argument
    """ Handler for uncaught exception.
    * https://docs.djangoproject.com/en/2.2/topics/http/urls/#error-handling
    * https://docs.djangoproject.com/en/2.2/ref/views/#the-500-server-error-view
    * https://docs.djangoproject.com/en/2.2/ref/urls/#handler500
    """
    r = custom_exception_handler(InternalServerError(), None)
    return JsonResponse(data=r.data,
                        status=r.status_code,
                        json_dumps_params={'ensure_ascii': False})


handler404 = not_found
handler500 = internal_server_error