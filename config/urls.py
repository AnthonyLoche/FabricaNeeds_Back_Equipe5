from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter
from fabricaNeeds.views import TotalViewSet, EstoqueViewSet, DemandasViewSet, RetirarEstoqueViewSet, EntradasEstoqueViewSet, ContribuinteViewSet, loginViewSet

router = DefaultRouter()
router.register(r"total", TotalViewSet)
router.register(r"estoque", EstoqueViewSet)
router.register(r"demandas", DemandasViewSet)
router.register(r"retirarEstoque", RetirarEstoqueViewSet)
router.register(r"entradasEstoque", EntradasEstoqueViewSet)
router.register(r"contribuinte", ContribuinteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', loginViewSet.as_view(), name='login'),
    path("", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
