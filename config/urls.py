from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Goodreads API Schemas",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="rashidi.peyman@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('accounts.urls')),
    path('books/', include('books.urls')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('silk/', include('silk.urls', namespace='silk'))
]


swagger = [

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

urlpatterns += swagger
