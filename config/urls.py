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
from core.fabricaNeeds.views import TotalViewSet, EstoqueViewSet, DemandasViewSet, PagamentosViewSet
from core.usuario.router import router as usuario_router


router = DefaultRouter()
router.register(r"total", TotalViewSet)
router.register(r"stock", EstoqueViewSet)
router.register(r"demands", DemandasViewSet)
# router.register(r"addStock", EntradasEstoqueViewSet)
router.register(r"payments", PagamentosViewSet)

urlpatterns = [
    path('admin', admin.site.urls),
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
    path("api/", include(usuario_router.urls)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
