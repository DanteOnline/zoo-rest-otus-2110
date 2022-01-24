import debug_toolbar
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

from animals import api_views, generic_views, view_sets, filter_views, pagination_views, views
from rest_framework.routers import DefaultRouter
from .doc_schemas import schema_view

# view sets
from users.views import UserListAPIView

router = DefaultRouter()
router.register(r'base', view_sets.KindViewSet, basename='kind')
router.register(r'model', view_sets.KindModelViewSet)
router.register(r'custom', view_sets.KindCustomViewSet)

# filter
filter_router = DefaultRouter()
filter_router.register('queryset', filter_views.KindQuerysetFilterViewSet)
filter_router.register('param', filter_views.KindParamFilterViewSet)
filter_router.register('django', filter_views.KindDjangoFilterViewSet)
filter_router.register('custom-django', filter_views.KindCustomDjangoFilterViewSet)
#

# # pagination
pagination_router = DefaultRouter()
pagination_router.register('pagenumber', pagination_views.KindPageNumberPaginatonViewSet)
pagination_router.register('limitoffset', pagination_views.KindLimitOffsetPaginatonViewSet)

urlpatterns = [
    # API views
    path('views/api-view/', api_views.KindAPIVIew.as_view()),
    path('views/func-api-view/', api_views.kind_view),
    # generic views
    path('generic/create/', generic_views.KindCreateAPIView.as_view()),
    path('generic/list/', generic_views.KindListAPIView.as_view()),
    path('generic/retrieve/<int:pk>/', generic_views.KindRetrieveAPIView.as_view()),
    path('generic/destroy/<int:pk>/', generic_views.KindDestroyAPIView.as_view()),
    path('generic/update/<int:pk>/', generic_views.KindUpdateAPIView.as_view()),
    path('generic/update/<int:pk>/', generic_views.KindUpdateAPIView.as_view()),
    # view sets
    path('viewsets/', include(router.urls)),
    # filters
    path('filters/', include(filter_router.urls)),
    path('filters/kwargs/<str:name>/', filter_views.KindKwargsFilterView.as_view()),
    # pagination
    path('pagination/', include(pagination_router.urls)),
    # other
    path('', include('animals.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    # versioning
    # (IN URL)
    re_path(r'^api/(?P<version>\d+\.\d+)/users/$', UserListAPIView.as_view()),
    # (NAMESPACE)
    path('api/users/0.1', include('users.urls', namespace='0.1')),
    path('api/users/0.2', include('users.urls', namespace='0.2')),
    # Еще есть HostNameVersioning
    # http://v1.example.com/bookings/.
    # docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
